def age_grouping(age_group):
    lessthanone = age_group.query('New_Age < 1')
    lessthanone = lessthanone['New_Age'].count()
    lessthanfour = age_group.query('New_Age > = 1 & New_Age <= 4 ')
    lessthanfour = lessthanfour['New_Age'].count()
    lessthanten = age_group.query(' New_Age > = 5 & New_Age <= 9 ')
    lessthanten = lessthanten['New_Age'].count()
    lessthanfourteen = age_group.query('New_Age > = 10 & New_Age <= 14 ')
    lessthanfourteen = lessthanfourteen['New_Age'].count()
    lessthannineteen = age_group.query(' New_Age > = 15 & New_Age <= 19 ')
    lessthannineteen = lessthannineteen['New_Age'].count()
    lessthantwenty_four = age_group.query(' New_Age > = 20 & New_Age <= 24 ')
    lessthantwenty_four = lessthantwenty_four['New_Age'].count()
    lessthantwenty_nine = age_group.query('  New_Age > = 25 & New_Age <= 29 ')
    lessthantwenty_nine = lessthantwenty_nine['New_Age'].count()
    lessthanthirty_four = age_group.query(' New_Age > = 30 & New_Age <= 34 ')
    lessthanthirty_four = lessthanthirty_four['New_Age'].count()
    lessthanthirty_nine = age_group.query('New_Age > = 35 & New_Age <= 39 ')
    lessthanthirty_nine = lessthanthirty_nine['New_Age'].count()
    lessthanforty_four = age_group.query(' New_Age > = 40 & New_Age <= 44 ')
    lessthanforty_four = lessthanforty_four['New_Age'].count()
    lessthanforty_nine = age_group.query(' New_Age > = 45 & New_Age <= 49 ')
    lessthanforty_nine = lessthanforty_nine['New_Age'].count()
    fiftyplus = age_group.query(' New_Age  >= 50 ')
    fiftyplus = fiftyplus['New_Age'].count()
    return fiftyplus, lessthanforty_four, lessthanforty_nine, lessthanfour, lessthanfourteen, lessthannineteen, lessthanone, lessthanten, lessthanthirty_four, lessthanthirty_nine, lessthantwenty_four, lessthantwenty_nine

def pregnant_grouping(age_group):
    lessthannineteen = age_group.query(' Current_Age > = 15 & Current_Age <= 19 ')
    lessthannineteen = lessthannineteen['Current_Age'].count()
    lessthantwenty_four = age_group.query(' Current_Age > = 20 & Current_Age <= 24 ')
    lessthantwenty_four = lessthantwenty_four['Current_Age'].count()
    lessthantwenty_nine = age_group.query('  Current_Age > = 25 & Current_Age <= 29 ')
    lessthantwenty_nine = lessthantwenty_nine['Current_Age'].count()
    lessthanthirty_four = age_group.query(' Current_Age > = 30 & Current_Age <= 34 ')
    lessthanthirty_four = lessthanthirty_four['Current_Age'].count()
    lessthanthirty_nine = age_group.query('Current_Age > = 35 & Current_Age <= 39 ')
    lessthanthirty_nine = lessthanthirty_nine['Current_Age'].count()
    lessthanforty_four = age_group.query(' Current_Age > = 40 & Current_Age <= 44 ')
    lessthanforty_four = lessthanforty_four['Current_Age'].count()
    lessthanforty_nine = age_group.query(' Current_Age > = 45 & Current_Age <= 49 ')
    lessthanforty_nine = lessthanforty_nine['Current_Age'].count()
    fiftyplus = age_group.query(' Current_Age  >= 50 ')
    fiftyplus = fiftyplus['Current_Age'].count()
    return fiftyplus, lessthanforty_four, lessthanforty_nine, lessthannineteen, lessthanthirty_four, lessthanthirty_nine, lessthantwenty_four, lessthantwenty_nine
