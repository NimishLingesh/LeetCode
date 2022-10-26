class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        es1_h = event1[0].split(":")[0]
        es1_m = event1[0].split(":")[1]
        ee1_h = event1[1].split(":")[0]
        ee1_m = event1[1].split(":")[1]
        
        es2_h = event2[0].split(":")[0]
        es2_m = event2[0].split(":")[1]
        ee2_h = event2[1].split(":")[0]
        ee2_m = event2[1].split(":")[1]
        if es1_h <= es2_h <ee1_h:
            return True
        elif es2_h == ee1_h:
            if es2_m <=ee1_m:
                return True
        if es2_h <= es1_h <ee2_h:
            return True
        elif es1_h==ee2_h:
            if es1_m <=ee2_m:
                return True
        return False
        