#!/usr/bin/env python

import config
import urllib
import simpleoauth2
import rs as qboxrs
import rscli
import digestoauth
import uptoken

config.ACCESS_KEY = '3cmgyvf_rMTPuhlFNm1FS89q94Fykmb5ZWZAm92a'
config.SECRET_KEY = 'xFmoT2RvsnISK7NoqJuYElWSmkHON6eRLz2h9SL1'

bucket = 'bukaopu'
key = 'test.jpg'
customer = 'end_user_id'
demo_domain = 'test_photos.dn.qbox.me'

tokenObj = uptoken.UploadToken(bucket, 3600, "", "", customer)
uploadToken = tokenObj.generate_token()
print "Upload Token is: %s" % uploadToken

resp = rscli.UploadFile(bucket, key, 'image/jpg', key, '', '', uploadToken)
print '\n===> UploadFile %s result:' % key
print resp

client = digestoauth.Client()
rs = qboxrs.Service(client, bucket)

resp = rs.Stat(key)
print '\n===> Stat %s result:' % key
print resp
