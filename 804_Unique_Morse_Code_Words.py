class Solution:
    table = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = set()
        for each_word in words:
            temp = ''
            for each_c in each_word:
                temp += Solution.table[each_c]
            result.add(temp)
        return (len(result))
        