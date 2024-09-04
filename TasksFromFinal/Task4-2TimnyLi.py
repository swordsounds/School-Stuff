import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5, 5))

x = ['Product A', 'Product B', 'Product C']
y = [100, 150, 200]

plt.title('Sales per Product')
plt.xlabel('Sales')
plt.ylabel('Products')
plt.bar(x, y)


if __name__ == '__main__':
    plt.show()