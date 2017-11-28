from pycake.api import CAKEApi


ckapi = CAKEApi(
        admin_domain='affiliates.nectarsleep.com', api_key='qCrge3XimmlXZlR3CW12g',
        use_https=False, json_response=True)

print ckapi.source_affiliate_summary(start_date='2017-10-1', end_date='2017-10-2')
