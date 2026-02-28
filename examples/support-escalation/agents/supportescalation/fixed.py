from cogsol.tools import BaseFixedResponse


class OfficeHoursFixed(BaseFixedResponse):
    key = "office_hours"
    response = (
        "IT Help Desk Hours:\n\n"
        "- Monday to Friday: 8:00 AM - 6:00 PM (local time)\n"
        "- Saturday: 9:00 AM - 1:00 PM (limited support)\n"
        "- Sunday and holidays: Closed\n\n"
        "For emergencies outside business hours, call the on-call line "
        "at +1 (555) 911-HELP."
    )


class ContactInfoFixed(BaseFixedResponse):
    key = "contact_info"
    response = (
        "IT Help Desk Contact Information:\n\n"
        "- Email: helpdesk@company.com\n"
        "- Phone: +1 (555) 100-HELP\n"
        "- Internal chat: #it-support on Teams\n"
        "- Self-service portal: https://helpdesk.company.com\n"
        "- Walk-in: Building A, 2nd Floor, Room 210"
    )


class OfficeLocationsFixed(BaseFixedResponse):
    key = "office_locations"
    response = (
        "IT Support Locations:\n\n"
        "- Headquarters: Building A, 2nd Floor, Room 210\n"
        "- West Campus: Building C, Ground Floor, Room 003\n"
        "- Remote Support: Available via Teams or phone\n\n"
        "Walk-in support is available during business hours. "
        "Please bring your employee badge for identification."
    )


class EmergencySupportFixed(BaseFixedResponse):
    key = "emergency_support"
    response = (
        "For IT Emergencies (system outages, security incidents):\n\n"
        "1. Call the emergency line: +1 (555) 911-HELP (24/7)\n"
        "2. Email: emergency@company.com\n"
        "3. If you suspect a security breach, also notify security@company.com\n\n"
        "Do NOT attempt to fix security incidents on your own. "
        "Disconnect affected devices from the network and wait for IT response."
    )
