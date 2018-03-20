class Solution(object):
    def constructRectangle(self, area):
        sq = int(area**.5)
        while area%sq!=0:
            sq-=1
        return [area//sq,sq]
