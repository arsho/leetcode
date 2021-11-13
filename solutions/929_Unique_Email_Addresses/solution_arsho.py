class Solution:
    def get_filtered_email_address(self, email):
        """
        :type email: str
        :rtype: str
        """
        local_name, domain = email.split("@")
        local_name = local_name.replace('.','')
        local_name = local_name.split("+")[0]
        return local_name+"@"+domain
        
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = {}
        for email in emails:
            email = self.get_filtered_email_address(email)
            unique_emails[email] = 1
        return len(unique_emails)
