
# Tanish K
# Bangalore Institute of Technology
# 2024
# 6362556584
# tanishkunigiri2002@gmail.com



class Hash_table():
    def __init__(self):
        self.hashs={}
        self.hashs['Product']=[]
        self.hashs['Unit Price in Rupees']=[]
        self.hashs['GST in %']=[]
        self.hashs['Quantity']=[]
    
    def Product(self, product):
        self.hashs['Product'].append(product)
    
    def Unit_Price(self,rupees):
        self.hashs['Unit Price in Rupees'].append(rupees)

    def GST(self, gst):
        self.hashs['GST in %'].append(gst/100)

    def quantity(self, qty):
        self.hashs['Quantity'].append(qty)

    def maxgst(self):
        arr=[]
        arrs=[]
        unisum=0
        for i in range(4):
            if self.hashs['Unit Price in Rupees'][i]>=500:
                arr.append(self.hashs['Unit Price in Rupees'][i]-(self.hashs['Unit Price in Rupees'][i]*0.05))
        
        ind=0
        
        for i in range(4):
            unisum+=self.hashs['Unit Price in Rupees'][i]+self.hashs['Unit Price in Rupees'][i] * self.hashs['GST in %'][i] * self.hashs['Quantity'][i]
            arrs.append(unisum)
        for i in range(len(arr)):
            if arrs[i]>arrs[ind]:
                ind=i
        return self.hashs['Product'][ind]
        
    
    def total_price(self):
        unisum=0
        for i in range(4):
            if self.hashs['Unit Price in Rupees'][i]>=500:
                self.hashs['Unit Price in Rupees'][i]=self.hashs['Unit Price in Rupees'][i]-(self.hashs['Unit Price in Rupees'][i]*0.05)
        
        for i in range(4):
            unisum+=self.hashs['Unit Price in Rupees'][i]+self.hashs['Unit Price in Rupees'][i] * self.hashs['GST in %'][i] * self.hashs['Quantity'][i]
        
        return unisum
    



            



def main():
    tab = Hash_table()
    tab.Product('Leather wallet')
    tab.Product('Umbrella')
    tab.Product('Cigarette')
    tab.Product('Honey')
    tab.Unit_Price(1100)
    tab.Unit_Price(900)
    tab.Unit_Price(200)
    tab.Unit_Price(100)
    tab.GST(18)
    tab.GST(12)
    tab.GST(28)
    tab.GST(0)
    tab.quantity(1)
    tab.quantity(4)
    tab.quantity(3)
    tab.quantity(2)
    y=tab.maxgst()
    print(y)
    x=tab.total_price()
    print(x)

if __name__=='__main__':
    main()