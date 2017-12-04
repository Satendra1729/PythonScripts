def TabToDicLst(tabSoup): 
    trs = tab.findAll('tr'); 
    headerLst = [re.sub('[^0-9a-zA-Z]',"",th.getText()) for th in trs[0].findAll('th')]; 
    temp = {}; 
    retLst = []; 
    for tr in trs : 
        for idx,td in enumerate(tr.findAll('td')) : 
            temp[headerLst[idx]] = td.getText(); 
        retLst.append(temp); 
    return retLst; 