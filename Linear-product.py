def linearSearchProduct(productaList,targetProduct):
  indices =[]

  for index, product in enumerate(productaList):
    if product == targetProduct: 
      indices.append(index)

  return indices


# Example usage:
products=["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = "apple"
result = linearSearchProduct(products,target)
print(result)