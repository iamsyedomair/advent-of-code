with open('input.txt', 'r') as file:
    content = file.read()
    paragraphs = content.split('\n\n')
    seeds = paragraphs[0]
    seedSoil = paragraphs[1]
    soilFertiliser = paragraphs[2]
    FeWa = paragraphs[3]
    WaLi = paragraphs[4]
    LiTe = paragraphs[5]
    TeHu = paragraphs[6]
    HuLo = paragraphs[7]
ml = [seedSoil,soilFertiliser,FeWa,WaLi,LiTe,TeHu,HuLo]
sl = []
dl = []
for k in range(len(ml)):
  t = ml[k]
  tl = t.split('\n')
  li = []
  li2 = []
  for i in range(1,len(tl)):
    dn,sn,rn = list(map(int,tl[i].split()))
    li.append([int(sn),int(sn)+int(rn)-1])
    li2.append([int(dn),int(dn)+int(rn)-1])
  sl.append(li)
  dl.append(li2)
# print(sl)
# print(dl)
seeds = seeds.split(':')[1]
seeds = list(map(int,seeds.replace("\n",' ').strip().split(' ')))
seds= []
for i in range(0,len(seeds),2):
   for k in range(seeds[i],seeds[i]+seeds[i+1]):
      seds.append(k)
# print(seds)
ans = []
for se in seds:
  for i in range(len(sl)):
    for k in range(len(sl[i])):
        if se>=sl[i][k][0] and se<= sl[i][k][1]:
          se+=dl[i][k][0]-sl[i][k][0]
          break
  ans.append(se)
print(min(ans))
