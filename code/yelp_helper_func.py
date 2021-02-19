def part_4_questions_answers(results_dataframe, reviews_dataframe):
# THIS FUNCTION IS CALLED TO DISPLAY THE PART 4 Q&A RESULTS
    
    most_reviewed_businesses = results_dataframe.sort_values('review_count',ascending=False)[0:5][['name','review_count']]
    highest_rating = results_dataframe['rating'].max()
    high_rated_bus_count = len(results_dataframe.loc[results_dataframe['rating']==highest_rating])#results_dataframe['rating'].max()])
    bus_percent_by_rating = results_dataframe.groupby('rating').count().apply(lambda x: 100*x/x.sum(), axis=0).business_id
    bus_percent_by_price = results_dataframe.groupby('price').count().apply(lambda x: 100*x/x.sum(), axis=0).business_id
    #results_dataframe.sort_values('review_count',ascending=False)[0:1]['business_id'][1]
    most_reviewed_text = reviews_dataframe.loc[reviews_dataframe['business_id']==results_dataframe.sort_values(by='review_count', ascending=False).head(1)['business_id'][1]].text
    max_rated_reviewed_biz = results_dataframe.loc[results_dataframe['rating']==results_dataframe['rating'].max()].sort_values(by='review_count', ascending=False).head(1).values[0][0]
    max_rated_review_text = reviews_dataframe.loc[reviews_dataframe['business_id']==max_rated_reviewed_biz].sort_values(by='time_created', ascending=False).head(1).text
    min_rated_reviewed_biz = results_dataframe.loc[results_dataframe['rating']==results_dataframe['rating'].min()].sort_values(by='review_count', ascending=False).head(1).values[0][0]
    min_rated_review_text = reviews_dataframe.loc[reviews_dataframe['business_id']==min_rated_reviewed_biz].sort_values(by='time_created', ascending=False).head(1).text

    print("1. Top 5 Most reviewed businesses are:")
    print(most_reviewed_businesses)
    print()
    print("2. Number of businesses with highest rating of {}: {}".format(highest_rating, high_rated_bus_count))
    print()
    print("3 & 4. Percent of businesses by Rating: {}".format(bus_percent_by_rating))
    print()
    print("5. Percent of businesses by Price: {}".format(bus_percent_by_price))
    print()
    print("6. Sample reviews of most reviewed business:")
    print(most_reviewed_text)
    print()
    print("7. Latest review of highest rated, highest reviewed business:")
    print(max_rated_review_text)
    print()
    print("8. Latest review of lowest rated, lowest reviewed business:")
    print(min_rated_review_text)
    return 
    
    
# INDIAN RESTAURANT PRICES
def indian_rest_price(indian_mia, indian_ny, indian_sj, indian_chi, indian_dc, indian_la):
    title = "Indian Restaurant Prices"
    labels = ["Miami", "New York", "Chicago", "San Jose", "Washington, D.C.", "Los Angeles"]
    value = "Price Value in Dollars"
    volume = "Amount of Restaurants"
    width = 0.35  # the width of the bars

    # MULTI BAR CHART PLOTS
    x_mia = list(indian_mia.groupby('price').count()['business_id'].index)
    y_mia = list(indian_mia.groupby('price').count()['business_id'].values)
    x_ny = list(indian_ny.groupby('price').count()['business_id'].index)
    y_ny = list(indian_ny.groupby('price').count()['business_id'].values)
    x_sj = list(indian_sj.groupby('price').count()['business_id'].index)
    y_sj = list(indian_sj.groupby('price').count()['business_id'].values)
    x_chi = list(indian_chi.groupby('price').count()['business_id'].index)
    y_chi = list(indian_chi.groupby('price').count()['business_id'].values)
    x_dc = list(indian_dc.groupby('price').count()['business_id'].index)
    y_dc = list(indian_dc.groupby('price').count()['business_id'].values)
    x_la = list(indian_la.groupby('price').count()['business_id'].index)
    y_la = list(indian_la.groupby('price').count()['business_id'].values)

    fig, axes = plt.subplots(figsize = (20, 15), ncols=3, nrows=2)
    fig.suptitle(title, size = 35)

    # TOP LEFT
    axes[0,0].bar(x_mia, y_mia, color = 'r')
    axes[0,0].set_title(labels[0], size=20)
    axes[0,0].set_xlabel(value, size=15)
    axes[0,0].set_ylabel(volume, size=15)
    axes[0,0].set_xticks(indian_mia['price'].sort_values().unique())

    # TOP MIDDLE
    axes[0,1].bar(x_ny, y_ny, color = 'b')
    axes[0,1].set_title(labels[1], size=20)
    axes[0,1].set_xlabel(value, size=15)
    axes[0,1].set_ylabel(volume, size=15)
    axes[0,1].set_xticks(indian_ny['price'].sort_values().unique())

    # TOP RIGHT
    axes[0,2].bar(x_chi, y_chi, color = 'y')
    axes[0,2].set_title(labels[2], size=20)
    axes[0,2].set_xlabel(value, size=15)
    axes[0,2].set_ylabel(volume, size=15)
    axes[0,2].set_xticks(indian_sj['price'].sort_values().unique())

    # BOTTOM LEFT
    axes[1,0].bar(x_sj, y_sj, color = 'darkorange')
    axes[1,0].set_title(labels[3], size=20)
    axes[1,0].set_xlabel(value, size=15)
    axes[1,0].set_ylabel(volume, size=15)
    axes[1,0].set_xticks(indian_chi['price'].sort_values().unique())

    # BOTTOM MIDDLE
    axes[1,1].bar(x_dc, y_dc, color = 'green')
    axes[1,1].set_title(labels[4], size=20)
    axes[1,1].set_xlabel(value, size=15)
    axes[1,1].set_ylabel(volume, size=15)
    axes[1,1].set_xticks(indian_dc['price'].sort_values().unique())

    # BOTTOM RIGHT
    axes[1,2].bar(x_la, y_la, color = 'maroon')
    axes[1,2].set_title(labels[5], size=20)
    axes[1,2].set_xlabel(value, size=15)
    axes[1,2].set_ylabel(volume, size=15)
    axes[1,2].set_xticks(indian_la['price'].sort_values().unique())
    # plt.savefig('indian_rest_prices.png')
    return


# RATINGS VS REVIEWS
def rating_vs_review(indian_sj, indian_dc, indian_la):
    title = "Ratings & Reviews Correlation"
    labels = ["San Jose", "Washington, D.C.", "Los Angeles"]
    value = "Markets"
    volume = "Reviews Baseline"

    y_sj = list(indian_sj['review_count'])
    y_dc = list(indian_dc['review_count'])
    y_la = list(indian_la['review_count'])

    fig, ax = plt.subplots(figsize= (20, 10))
    
    ax.boxplot([y_sj, y_dc, y_la], labels = labels, patch_artist = True)
    ax.set_facecolor('bisque')
    ax.set_title(title, size=30)
    ax.set_xlabel(value, size=20)
    ax.set_ylabel(volume, size=20)
    ax.set_ylim(0, indian_dc['review_count'].max())
    ax.yaxis.grid(True)

    # plt.savefig('ratings_review_correlation')
    return


# MEAN PRICES OF TARGET MARKETS
def target_mean_price(indian_sj, indian_dc, indian_la, indian_ny, indian_chi, indian_mia):
    title = "Target Market Mean Price"
    labels = ["New York", "Miami", "Chicago", "San Jose", "D.C.", "Los Angeles"]
    value = "Markets"
    volume = "Mean Price Value"

    ny_mean = indian_ny['price'].mean()
    mia_mean = indian_mia['price'].mean()
    sj_mean = indian_sj['price'].mean()
    chi_mean = indian_chi['price'].mean()
    dc_mean = indian_dc['price'].mean()
    la_mean = indian_la['price'].mean()

    x_vals = [labels[0], labels[1], labels[2], labels[3], labels[4], labels[5]]
    y_vals = [ny_mean, mia_mean, chi_mean, sj_mean, dc_mean, la_mean]

    fig, ax = plt.subplots(figsize = (20,10))

    ax.bar(labels, y_vals, color=['grey', 'grey', 'grey', 'darkorange', 'green', 'maroon'])
    ax.set_title(title, size=20)
    ax.set_xlabel(value, size=15)
    ax.set_ylabel(volume, size=15)

    # plt.savefig('mean_price_target')
    return


# TOP 3 MARKETS REVIEWS
def top_3_market_reviews(indian_sj, indian_dc, indian_la):
    title = "Top 3 Markets Review Distribution"
    labels = ["San Jose", "D.C.", "Los Angeles"]
    ticks = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    value = "Top 3 Markets"
    volume = "Review Counts; Price = 3"

    sj_rev = list(indian_sj.query('price == 3')['review_count'])
    sj_rat = list(indian_sj.query('price == 3')['rating'])
    dc_rev = list(indian_dc.query('price == 3')['review_count'])
    dc_rat = list(indian_dc.query('price == 3')['rating'])
    la_rev = list(indian_la.query('price == 3')['review_count'])
    la_rat = list(indian_la.query('price == 3')['rating'])

    fig, axes = plt.subplots(figsize = (20, 15), ncols=3)
    fig.suptitle(title, size = 35)

    # BOTTOM LEFT
    axes[0].scatter(sj_rat, sj_rev, color = 'darkorange')
    axes[0].set_title(labels[0], size=20)
    axes[0].set_xlabel(value, size=20)
    axes[0].set_ylabel(volume, size=20)
    axes[0].set_xticks(ticks)

    # BOTTOM MIDDLE
    axes[1].scatter(dc_rat, dc_rev, color = 'green')
    axes[1].set_title(labels[1], size=20)
    axes[1].set_xlabel(value, size=20)
    axes[1].set_ylabel(volume, size=20)
    axes[1].set_xticks(ticks)

    # BOTTOM RIGHT
    axes[2].scatter(la_rat, la_rev, color = 'maroon')
    axes[2].set_title(labels[2], size=20)
    axes[2].set_xlabel(value, size=20)
    axes[2].set_ylabel(volume, size=20)
    axes[2].set_xticks(ticks)

    # plt.savefig('top_3_review_dist')
    return


# TOP 3 MARKETS RATINGS
def top_3_market_ratings(indian_sj, indian_dc, indian_la):
    title = "Top 3 Markets Review Distribution"
    labels = ["San Jose", "D.C.", "Los Angeles"]
    ticks = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    value = "Top 3 Markets"
    volume = "Review Counts; Price = 3"

    sj_rev = list(indian_sj.query('price == 3')['review_count'])
    sj_rat = list(indian_sj.query('price == 3')['rating'])
    dc_rev = list(indian_dc.query('price == 3')['review_count'])
    dc_rat = list(indian_dc.query('price == 3')['rating'])
    la_rev = list(indian_la.query('price == 3')['review_count'])
    la_rat = list(indian_la.query('price == 3')['rating'])

    fig, axes = plt.subplots(figsize = (20, 15), ncols=3)
    fig.suptitle(title, size = 35)

    # BOTTOM LEFT
    axes[0].bar(sj_rat, sj_rev, color = 'darkorange')
    axes[0].set_title(labels[0], size=20)
    axes[0].set_xlabel(value, size=20)
    axes[0].set_ylabel(volume, size=20)
    axes[0].set_xticks(ticks)

    # BOTTOM MIDDLE
    axes[1].bar(dc_rat, dc_rev, color = 'green')
    axes[1].set_title(labels[1], size=20)
    axes[1].set_xlabel(value, size=20)
    axes[1].set_ylabel(volume, size=20)
    axes[1].set_xticks(ticks)

    # BOTTOM RIGHT
    axes[2].bar(la_rat, la_rev, color = 'maroon')
    axes[2].set_title(labels[2], size=20)
    axes[2].set_xlabel(value, size=20)
    axes[2].set_ylabel(volume, size=20)
    axes[2].set_xticks(ticks)

    # plt.savefig('top_3_review_dist_bar')
    return