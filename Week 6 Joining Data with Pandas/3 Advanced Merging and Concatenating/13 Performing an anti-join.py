In our music streaming company dataset, each customer is assigned an employee representative to assist them. In this exercise, filter the employee table by a table of top customers, returning only those employees who are not assigned to a customer. The results should resemble the results of an anti-join. The company's leadership will assign these employees additional training so that they can work with high valued customers.

The top_cust and employees tables have been provided for you.

Instructions 1/3
35 XP
Merge employees and top_cust with a left join, setting indicator argument to True. Save the result to empl_cust.

In
our
music
streaming
company
dataset, each
customer is assigned
an
employee
representative
to
assist
them.In
this
exercise, filter
the
employee
table
by
a
table
of
top
customers, returning
only
those
employees
who
are
not assigned
to
a
customer.The
results
should
resemble
the
results
of
an
anti - join.The
company
's leadership will assign these employees additional training so that they can work with high valued customers.

The
top_cust and employees
tables
have
been
provided
for you.

Instructions
1 / 3
35
XP
Merge
employees and top_cust
with a left join, setting indicator argument to True.Save the result to empl_cust.


# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid',
                            how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid',
                            how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] =='left_only', 'srid']

# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcsk to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))

