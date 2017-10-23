
operator_count = Counter(df['Operator'].dropna()).most_common(10)
operator_keys = [operator[0] for operator in operator_count]
operator_val = [operator[1] for operator in operator_count]

fig,ax = plt.subplots(figsize = (8,6))
sns.barplot(x = operator_keys, y = operator_val)
plt.title('Top 10 operator')
plt.ylabel('Count')
plt.xlabel('Operator')
ticks = plt.setp(ax.get_xticklabels(),rotation=90)
plt.show()