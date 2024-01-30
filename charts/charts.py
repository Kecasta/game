import matplotlib.pyplot as plt


def generate_pie_chart():
    label = ['A', 'B', 'C']
    values = (200, 300, 120)

    fig, ax = plt.subplosts()
    ax.pie(values,label=label)
    plt.savefig('pie.png')
    plt.close
