class MaximumTemperature:
    def __init__(self,temps):
        self.temps = temps
    
    def get_max_temp(self):
        return max(self.temps)
    
    def get_min_temp(self):
        return min(self.temps)
    
    def get_mean_temp(self):
        sum=0
        for temp in self.temps:
            sum +=temp
        return sum/len(self.temps)
    
    
def main():
    data = open('./files/temperature.txt','r')
    lines = data.readlines()
    max_temps = []
    for line in lines:
        arr_temp=line.split(' ')
        max_temps.append(float(arr_temp[3]))
        
    print('\n',max_temps)
    maxTemp = MaximumTemperature(max_temps)
    print(f'The max temperature for given data is: {maxTemp.get_max_temp()}')
    print(f'The min temperature for given data is: {maxTemp.get_min_temp()}')
    print(f'The mean temperature for given data is: {maxTemp.get_mean_temp()}\n')



if __name__ == "__main__":
    main()