# Remote Work Setup Guide

Everything you need to work productively from outside the office.

## Required Tools

Before starting remote work, ensure you have:

- A company-issued laptop with the latest updates installed
- GlobalProtect VPN client (available in Software Center)
- Microsoft Teams for communication
- Microsoft Outlook for email
- MFA authenticator app configured on your phone

## VPN Configuration

1. Open GlobalProtect from the system tray.
2. Enter the portal address: vpn.company.com
3. Sign in with your corporate email and password.
4. Approve the MFA notification on your phone.
5. Wait for the "Connected" status to appear.

The VPN must be connected to access internal resources such as network drives, intranet sites, and internal applications.

## Home Network Recommendations

- Use a wired Ethernet connection when possible for stability.
- If using Wi-Fi, sit close to your router.
- Minimum recommended bandwidth: 25 Mbps download, 10 Mbps upload.
- Avoid using public Wi-Fi for work. If unavoidable, always use the VPN.

## Accessing Internal Applications

With VPN connected, you can access:

- Intranet: https://intranet.company.com
- Helpdesk Portal: https://helpdesk.company.com
- Network Drives: Use File Explorer to navigate to \\fileserver\share
- Internal databases and tools function as if you were in the office

## Remote Desktop

To connect to your office desktop remotely:

1. Connect to the VPN first.
2. Open Remote Desktop Connection (search "mstsc" in Start).
3. Enter your office computer name (found on the asset sticker).
4. Sign in with your corporate credentials.

## Troubleshooting Remote Access

- If VPN connects but internal sites are unreachable, try disconnecting and reconnecting.
- If VPN fails entirely, check your internet connection first, then try restarting GlobalProtect.
- For persistent issues, contact the Help Desk with your VPN client version and error message.
