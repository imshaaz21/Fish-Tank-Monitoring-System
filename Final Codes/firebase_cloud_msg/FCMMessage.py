import firebase_admin
from firebase_admin import credentials, messaging

config = {
  "type": "service_account",
  "project_id": "fishtankapp-88d91",
  "private_key_id": "a6d5e11ac9f1002e6eb7c7008891a7499859fde3",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDTPJy+gVCpB3dd\nQ9bRcZAllirf2kK+Zgjky0Goynvx2QBc42OlnoJp+3nWJau7FCJPsUqThr4goxeZ\njPf2PoaduardElsu39B8ko4mzM3won9btd/ZKjcs2w3pUyZvthNcrzb1WU+tqZoQ\nsn2GrcOAhk6Afkdpu8FgTYR7MyHFJYl9Sn0QB9mn7KgXBHegMNVQRnLKkcH7ev65\ngQYDBY0qLzq2G9eALeSAm955+U9kWizYp6kra1jEmqkrNvUFvqKJA4fMVGKpOZ5+\ni5IzErm+x4fj98CmG7lSdA6O46Sojzhm7KYQHadIpsnX6zG+UMEF1OGQMQdg1Up/\n25JR2tknAgMBAAECggEART6z1UFX2ykO6HxiEaNsEN4yrNIEGh0hojq9CeNikQvF\nMi36TuLwtmRQ8rHDo158xuoD2+uKLPG5vUS4Tjj98PtZtwGa8Xk+A3AZeD+f7Nef\n70TmHe7YSnR+kXOIAIvLuhDX78K4u2GDFyEjw//3PA0K89UxfMgnInYWzTocQl8s\nriB9IuT43lkOqF7PNuWV3PU2HvQ/pgdsjHVIn7j+p3Ln7RVFtbHK4B8LxbvqNyou\nNQUBJhs569WdKAPniYo6e3ivOzHVF25AAnKIMnPepVpFp1GJIEqmK1rSVUNEMLl0\nFYHvi6BUVYQ5ZTUSlTCpcD6GnuvrOz6BDNQgYQrfOQKBgQDw4DwNfkk1h3lf143n\n0z59ZKBkwmK1P16umpoMs3OoUjZHBQkQr+uodkhii60cqB+oFsICRhJTkMWxyOfL\nd9Rzc8SHOAVZr2gWuFhZaTWp9Nl6lA+H4dUIZVIo9xcqhS7HK5/aJ+4fZvNY9W9+\nl6UsxrZhdFF9LhpoxSd+AOnz+QKBgQDgf/eVYWxsNmaUXnOOzx+s26yYh/S5ndY6\nNVegvoHwkFaGVmtJPGEvkjZo+A4CMCNQPyOSck4WQnn1AtxBKS29+o7Wfjcp5Z9e\nwzVppRJa+I19WK/iCxEIhYuxIBIAlPo0SwXoKMve6ziia7vE81tDTSy0v7y+MTU4\nmAgIK/A+HwKBgH65if6TVRK7bmi07+xqH7M6sIOyHNo8N6Tmo2tRMeT5M6MTjBxi\nYTnk2No3n+C2tsjpCDLICLY8MTYCe6h5J6WB34BAQdhYRwvE+n43ssryjURHBxC3\nCCv9mkcBEAgHv397fQL6BPYyZI6FuZ3BTF4NQUBuQLz591ztdIR/GJaJAoGBAKux\n8t4yNkPEj0tluSc9TVJcZ3H4eLgE+LRn2266hJJBMYtoSIEoRoOlZSt+mugdfMSA\npWn5NbNcf/1chKrpHWywVdHBkdrfHLXSweTcNF+SvFNjIpDUOeC0khOTHXGIfprD\nze6yVMlWSGgf0Old3Sxpt4k9ItKqu7NewrXNNN2tAoGAGHQfbreDtJM++hFvUcxD\neEPQwDawqdO0/sHU9SB99gsE+wH19jzSBT1saDT3DWkiEXg/dxUNGz96QPeszHRL\nx3kB8mizjCRHXP1cpmNuijmt/58R48JFMtzPP5G9E/Ku3t9iRbP96M0RJsXFTUzR\n8t3SXs4ASVOnkr+D9WRJ6QI=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-rtm0h@fishtankapp-88d91.iam.gserviceaccount.com",
  "client_id": "100500891628555041108",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-rtm0h%40fishtankapp-88d91.iam.gserviceaccount.com"
}
cred = credentials.Certificate(
    "/home/pi/Final Codes/firebase_cloud_msg/keys.json")
firebase_admin.initialize_app(cred)


def sendPush(title, msg, registration_token, dataObject=None):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
