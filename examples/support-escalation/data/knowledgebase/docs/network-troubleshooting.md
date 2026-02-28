# Network Troubleshooting Guide

Step-by-step guide for resolving common network connectivity issues in the corporate environment.

## Wi-Fi Connection Issues

1. Check that Wi-Fi is enabled on your device.
2. Forget the current network and reconnect to "CorpNet-Secure".
3. Ensure you are using your corporate credentials (not personal).
4. If prompted, accept the security certificate.
5. Restart your device if the issue persists.

## Wired Connection Issues

1. Check that the Ethernet cable is securely connected at both ends.
2. Try a different Ethernet port on the wall plate.
3. Try a different cable if available.
4. Open a command prompt and run `ipconfig /release` then `ipconfig /renew`.
5. Contact IT if the port indicator light does not turn on.

## DNS Resolution Failures

If you can ping IP addresses but not hostnames:

1. Open Command Prompt as administrator.
2. Run `ipconfig /flushdns` to clear the DNS cache.
3. Run `nslookup company.com` to test DNS resolution.
4. If DNS fails, manually set DNS to 10.0.0.53 and 10.0.0.54.

## Slow Network Performance

- Close bandwidth-heavy applications (video streaming, large downloads).
- Disconnect from the VPN if you are in the office.
- Move closer to the Wi-Fi access point if using wireless.
- Check the service status page at https://status.company.com for outages.

## Network Drive Access

If you cannot access a mapped network drive:

1. Open File Explorer and right-click the drive, select "Disconnect".
2. Re-map the drive: open Run (Win+R), type `\\fileserver\share`.
3. Enter your corporate credentials if prompted.
4. If the server is unreachable, check https://status.company.com.
