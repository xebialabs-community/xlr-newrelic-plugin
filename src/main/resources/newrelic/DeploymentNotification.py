#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import json
import urllib2


def printData(url, data):
    print
    print 'URL:'
    print '```'
    print url
    print '```'
    print 'Data:'
    print '```'
    print data
    print '```'

# Initialize variables & check parameters
response = ''
url = server['url']
apiKey = server['apiKey']
proxyUrl = server['proxyUrl']
if not url.strip():
    print 'Error!'
    print 'Server configuration url undefined\n'
    sys.exit(100)
if not apiKey.strip():
    print 'Error!'
    print 'Server configuration apiKey undefined\n'
    sys.exit(100)
if not revision.strip():
    print 'Error!'
    print 'Parameter Revision undefined\n'
    sys.exit(200)
if not applicationId.strip():
    print 'Error!'
    print 'Parameter Application ID undefined\n'
    sys.exit(200)

# Set up proxy
# proxyUrl format: 'http:// username:password@proxyurl:proxyport'
if proxyUrl:
    proxy = urllib2.ProxyHandler({'http': proxyUrl.strip(), 'https': proxyUrl.strip()})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

# Call Newrelic REST API
try:
    endpoint = "%s/v2/applications/%s/deployments.json" % (url,applicationId)
    request = urllib2.Request(endpoint)
    request.add_header('Content-Type', 'application/json')
    request.add_header('X-Api-Key', apiKey) 
    postdata = {
                   "deployment": {
                   "revision": revision,
                   "changelog": changelog,
                   "description": description,
                   "user": user 
                 }
                }
    data = json.dumps(postdata)
    response = urllib2.urlopen(request, data)
except urllib2.HTTPError as error:
    print 'HTTP %s error!' % error.code
    print 'Reason: %s' % error.read()
    printData(endpoint, data)
    sys.exit(300)
except urllib2.URLError as error:
    print 'Network error!'
    print 'Reason: %s' % error.reason
    printData(endpoint, data)
    sys.exit(400)

# Print output
print 'Newrelic deployment notification %s sent successfully' % revision
print '```'
print 'Changelog entry was %s ' % changelog
print '```'
sys.exit(0)
