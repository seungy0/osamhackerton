def PointinPolygon(polyogn, x,y): #예를 들어 삼각형((1,2),(0,0),(2.1))이라면 polygon은 [[1,2],[0,0],[2,1]]
  n=len(polygon)
  x1=x
  y1=y
  inPolygon= False
  icrosses = 0
  for i in range(n):
    j= (i+1)%n
    if (polygon[i][1]>y1)!=polygon[j][1]>y1):
      meetX=(((polygon[j][0]-polygon[i][0])/polygon[j][1]-polygon[i][1])*(y1-polygon[1]))+polygon[i][0]
      if x1<meetX:
        icrosses+=1
    if 0==(icrosses%2):
      inPolygon=False
    else:
      inPolygon=True
    return inPolygon
