


mean_y = 170
mean_x = 75       
r = 0.60         
sd_y = 6.0        
sd_x = 6.0       


byx = r * sd_y / sd_x   
bxy = r * sd_x / sd_y  


ht_amit = mean_y - byx * (mean_x - 50)


wt_sumit = mean_x - bxy * (mean_y - 150)

# Display results
print(f"Amit's predicted height (for 50 kg): {ht_amit:.2f} cm")
print(f"Sumit's predicted weight (for 150 cm): {wt_sumit:.2f} kg")
