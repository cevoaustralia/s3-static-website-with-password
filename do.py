#!/usr/bin/env python3

import boto3

def create_rr(domain, name, type, val):
    print(f'Creating {name} {type} in {domain} with val {val}')
    r53 = boto3.client('route53')
    zones = r53.list_hosted_zones_by_name(DNSName=domain)
    zoneid = zones['HostedZones'][0]['Id']
    r53.change_resource_record_sets(
        HostedZoneId=zoneid,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': name,
                        'TTL': 300,
                        'Type': type,
                        'ResourceRecords': [
                            {
                                'Value': val
                                }
                            ]
                        }
                    }
                ],
            }
        )

acm = boto3.client('acm')
res = acm.list_certificates()
if len(res['CertificateSummaryList']) == 0:
    print('No certs waiting')

found = False
for cert in res['CertificateSummaryList']:
    if cert['DomainName'] != "www.thanatopho.be":
        continue

found = True
desc = acm.describe_certificate(CertificateArn=cert['CertificateArn'])
for opts in desc['Certificate']['DomainValidationOptions']:
    if opts['ValidationMethod'] == 'DNS':
        rr_name = opts['ResourceRecord']['Name']
        rr_type = opts['ResourceRecord']['Type']
        rr_val  = opts['ResourceRecord']['Value']

        create_rr('thanatopho.be', rr_name, rr_type, rr_val)

