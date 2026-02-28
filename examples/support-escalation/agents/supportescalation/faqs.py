from cogsol.tools import BaseFAQ


class PasswordResetFAQ(BaseFAQ):
    question = "How do I reset my password?"
    answer = (
        "To reset your password:\n\n"
        "1. Go to https://password.company.com\n"
        "2. Click 'Forgot Password'\n"
        "3. Enter your employee email address\n"
        "4. Follow the link sent to your email\n"
        "5. Create a new password (min. 12 characters, one uppercase, "
        "one number, one special character)\n\n"
        "If you are locked out, contact the Help Desk to verify your "
        "identity and unlock your account."
    )


class VpnAccessFAQ(BaseFAQ):
    question = "How do I connect to the company VPN?"
    answer = (
        "To connect to the VPN:\n\n"
        "1. Install GlobalProtect from the Software Center\n"
        "2. Open GlobalProtect and enter portal: vpn.company.com\n"
        "3. Sign in with your corporate credentials\n"
        "4. Approve the MFA prompt on your authenticator app\n\n"
        "The VPN is required for accessing internal resources when "
        "working remotely. If connection fails, check that your "
        "internet is working and your credentials are correct."
    )


class EquipmentRequestFAQ(BaseFAQ):
    question = "How do I request new equipment like a laptop or monitor?"
    answer = (
        "To request new equipment:\n\n"
        "1. Log in to the self-service portal: https://helpdesk.company.com\n"
        "2. Go to Service Catalog > Hardware Requests\n"
        "3. Select the item you need and fill out the request form\n"
        "4. Your manager will receive an approval notification\n\n"
        "Standard equipment is delivered within 5-7 business days after "
        "approval. Urgent requests require manager escalation."
    )


class SoftwareInstallFAQ(BaseFAQ):
    question = "How do I install new software on my work computer?"
    answer = (
        "To install approved software:\n\n"
        "1. Open Software Center (pre-installed on all company devices)\n"
        "2. Browse or search for the application you need\n"
        "3. Click 'Install' and wait for completion\n\n"
        "If the software is not listed in Software Center, submit a "
        "request at https://helpdesk.company.com > Service Catalog > "
        "Software Requests. The IT team will review and approve within "
        "2 business days."
    )


class TicketingProcessFAQ(BaseFAQ):
    question = "How does the ticketing system work?"
    answer = (
        "Our ticketing system tracks all IT requests:\n\n"
        "1. Tickets are created automatically when you email helpdesk@company.com "
        "or submit a request via the portal\n"
        "2. You receive a ticket number for tracking\n"
        "3. A technician is assigned based on the issue category\n"
        "4. You can check status at https://helpdesk.company.com > My Tickets\n\n"
        "Response times: Critical (1 hour), High (4 hours), "
        "Medium (1 business day), Low (3 business days)."
    )


class MobileEmailFAQ(BaseFAQ):
    question = "How do I set up work email on my personal phone?"
    answer = (
        "To set up corporate email on your mobile device:\n\n"
        "1. Install Microsoft Outlook from your app store\n"
        "2. Open Outlook and tap 'Add Account'\n"
        "3. Enter your work email address\n"
        "4. Sign in with your corporate credentials\n"
        "5. Approve the MFA prompt\n"
        "6. Accept the device management policy when prompted\n\n"
        "Note: The company MDM policy will be applied to your device. "
        "This requires a screen lock and allows remote wipe of "
        "corporate data only."
    )
