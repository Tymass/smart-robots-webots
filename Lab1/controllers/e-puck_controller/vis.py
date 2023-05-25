import matplotlib.pyplot as plt


def visualization():
    # Read estimated data from robot file, (data format: x, y, speed \n)
    data = []
    with open('e-puck_controller/dane.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(list(map(float, line.strip().split(','))))

    data = list(map(list, zip(*data)))
    x = data[0]
    y = data[1]
    speed = data[2]

    # Read actuall data from supervisor file, (data format: x, y \n)
    supervisor_data = []
    with open('supervisor_controller/dane_z_supervisora.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            supervisor_data.append(list(map(float, line.strip().split(','))))

    #supervisor_data = list(map(list, zip(*supervisor_data)))
    sup_x = []
    sup_y = []
    for i in range(len(supervisor_data)):
        sup_x.append(supervisor_data[i][0])
        sup_y.append(supervisor_data[i][1])

    # Plots of robot position and speed
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 8)

    ax1.plot(x, y, label='Estimated position')
    ax1.plot(sup_x, sup_y, label='Actuall position', linestyle='dashdot')
    ax1.set_title('Robot Position')
    ax1.grid(True)
    ax1.set(xlabel='X position', ylabel='Y position')
    ax1.set_aspect('equal')
    ax1.legend()

    ax2.plot(speed, label='Robot speed')
    ax2.set_title('Estimated robot speed')
    ax2.grid(True)
    ax2.set(xlabel="Time step", ylabel="m/s")
    ax2.legend()

    ''' 
    # Plot of just robot position
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, label='Estimated position')
    #plt.plot(next_x, next_y, label='Estimated next position', linestyle='dashed')
    plt.plot(sup_x, sup_y, label='Actuall position', linestyle='dashdot')
    plt.xlabel('X position')
    plt.ylabel('Y position')
    # plt.axis('square')
    plt.legend()
    plt.grid(True)
    plt.title('Robot Position')
    
    '''
    plt.show()


visualization()
