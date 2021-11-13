class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        for cpdomain in cpdomains:
            visits, domains = cpdomain.split(" ")
            visits = int(visits)
            domain_words = domains.split(".")
            domain_words_length = len(domain_words)
            domains = []
            for i in range(domain_words_length):
                domains.append(".".join(domain_words[i:]))
            for domain in domains:
                d[domain] = d.get(domain, 0) + visits
        result=[]
        for key in d.keys():
            result.append("{} {}".format(d[key], key))
        return result
