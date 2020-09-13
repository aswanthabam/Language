import re 
class HyperTextMarkup:
    
    def __init__(self,data):
        data = data.replace("\n","")
        tags1 = re.findall("<.*?>",data)
        tags = []
        self.html = data
        for x in tags1:
            if "!doctype html" in x.lower():
                self.Doctype = x
                continue
            tags.append(x)
            
            continue
        self.tags = tags
        self.selfClosing = []
        tag = []
        self.closingTags = []
        self.AllTagData = {}
        mg = []
        var2 = re.compile(r"<[^>]+>")
        
        self.removeAllTags = var2.sub("",data)
        for x in tags:
            if "</" not in x and "/" in x:
                self.selfClosing.append(x)
                continue
            if "</" in x:
                self.closingTags.append(x)
                continue
            
            if " " in x:
                
               
                attributes = []
                try:
                    var4 = x.split(" ")
                    i = 0
                
                    for y in var4:
                       
                        i = i + 1
                        if i == 1:continue
                        var3 = y.replace(">","").replace(">","").split("=")
                        
                        attributes.append((var3[0],var3[1]))
                        
                except:
                    attributes = []
                x = x.split(" ")[0]+">"
            else:
                attributes = []
                    
            if x.replace(">","").replace("<","") in mg:
               
                vr = self.AllTagData[x.replace("<","").replace(">","")]["attributes"]
                lst = [y for y in vr.items()]
                last = lst[len(lst)-1][0] + 1
                mrr = {last:attributes}
                vr.update(mrr)
                
                continue
            tag.append(x)
            #print(x)
            contents = re.findall(f'<{x.split(" ")[0].replace(">","").replace("<","")}.*?>(.*?){x.replace("<","</")}',data)
            mg.append(x.replace("<","").replace(">","").split(" ")[0])
            formated = {x.replace("<","").replace(">",""):{"contents":contents,"TotalNumberOfTags":len(contents),"attributes":{1:attributes}}}
            self.AllTagData.update(formated)
        
        
        mg = []
        for x in self.selfClosing:
            if " " in x:
                tag = x.split(" ")[0].replace("<","").replace(">","").replace("/","")
            else:
                tag = x.replace(">","").replace("<","").replace("/","")
                
                
            
            attributes = []
            if " " in x:
                var1 = x.split(" ")
                try:
                    for y in var1[1:]:
                        try:
                            var2 = y.split("=")
                        except:
                            var2 = None
                        attr = var2[0]
                        try:
                            val = var2[1].replace(">","").replace("/","")
                        except:
                            val = None
                        attributes.append((attr,val))
                except:
                    attributes = []
            contents = None
            if tag in mg:
                var3 = self.AllTagData[tag]["attributes"]
                var4 = [g for g in var3]
                last = var4[len(var4)-1] + 1
                ff = {last:attributes}
                var3.update(ff)
                continue
            the_all_tag = re.findall(f"<{tag}.*?/>",data)
            fff = {tag:{"contents":contents,"TotalNumberOfTags":len(the_all_tag),"attributes":{1:attributes}}}
            self.AllTagData.update(fff)
            mg.append(tag)
        return None
    
    def get(self,tag):
        self.RequestedTag = tag
        self.Data = self.AllTagData[tag]
        self.contents = self.Data["contents"]
        self.NoOfTags = self.Data["TotalNumberOfTags"]
        self.attributes = self.Data["attributes"]
        self.loop = []
        i = 0
        for x in self.contents:
            i = i + 1
            formated = {"content":x,"attribute":self.attributes[i],"Num":i}
            self.loop.append(formated)
            continue
        lst = []
        for x in self.tags:
            if "</" in x:
                continue
            if " " in x:
                m = x.split(" ")[0] + ">"
            else:
                m = x
            if m.replace("<","").replace(">","") == tag:
                lst.append(x)
                continue
            continue
        self.getedData = lst
        return self.getedData
    def content(self,no):
        return self.contents[no]
    def attribute(self,no):
        return self.attributes[no]

#closed class HyperTextMarkup
