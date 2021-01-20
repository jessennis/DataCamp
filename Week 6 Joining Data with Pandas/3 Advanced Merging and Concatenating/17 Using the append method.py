Using the append method
The .concat() method is excellent when you need a lot of control over how concatenation is performed. However, if you do not need as much control, then the .append() method is another option. You'll try this method out by appending the track lists together from different Metallica albums. From there, you will merge it with the invoice_items table to determine which track sold the most.

The tables tracks_master, tracks_ride, tracks_st, and invoice_items have loaded for you.

Instructions
100 XP
Use the .append() method to combine (in this order)tracks_ride, tracks_master, and tracks_st together vertically, and save to metallica_tracks.
Merge metallica_tracks and invoice_items on tid with an inner join, and save to tracks_invoices.
For each tid and name in tracks_invoices, sum the quantity sold column, and save as tracks_sold.
Sort tracks_sold in descending order by the quantity column, and print the table.

# Use the .append() method to combine the tracks tables
metallica_tracks = ____.append(____, sort=False)

# Merge metallica_tracks and invoice_items
tracks_invoices = ____

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid','name']).agg(____)

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values(____))
