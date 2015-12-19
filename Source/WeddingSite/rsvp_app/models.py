from django.db import models

# Create your models here.

class contact(models.Model):
    Alabama	= 'AL'
    Montana	= 'MT'
    Alaska = 'AK'
    Nebraska = 'NE'
    Arizona	= 'AZ'
    Nevada = 'NV'
    Arkansas = 'AR'
    New_Hampshire = 'NH'
    California = 'CA'
    New_Jersey = 'NJ'
    Colorado = 'CO'
    New_Mexico = 'NM'
    Connecticut = 'CT'
    New_York = 'NY'
    Delaware = 'DE'
    North_Carolina = 'NC'
    Florida = 'FL'
    North_Dakota = 'ND'
    Georgia = 'GA'
    Ohio = 'OH'
    Hawaii = 'HI'
    Oklahoma = 'OK'
    Idaho = 'ID'
    Oregon = 'OR'
    Illinois = 'IL'
    Pennsylvania = 'PA'
    Indiana = 'IN'
    Rhode_Island = 'RI'
    Iowa = 'IA'
    South_Carolina = 'SC'
    Kansas = 'KS'
    South_Dakota = 'SD'
    Kentucky = 'KY'
    Tennessee = 'TN'
    Louisiana = 'LA'
    Texas = 'TX'
    Maine = 'ME'
    Utah = 'UT'
    Maryland = 'MD'
    Vermont = 'VT'
    Massachusetts = 'MA'
    Virginia = 'VA'
    Michigan = 'MI'
    Washington = 'WA'
    Minnesota = 'MN'
    West_Virginia = 'WV'
    Mississippi = 'MS'
    Wisconsin = 'WI'
    Missouri = 'MO'
    Wyoming = 'WY'
    
    STATE_CHOICES = (
                     (Alabama, 'Alabama'),
                     (Alaska, 'Alaska'),
                     (Arizona, 'Arizona'),
                     (Arkansas, 'Arkansas'),
                     (California, 'California'),
                     (Colorado, 'Colorado'),
                     (Connecticut, 'Connecticut'),
                     (Delaware, 'Delaware'),
                     (Florida, 'Florida'),
                     (Georgia, 'Georgia'),
                     (Hawaii, 'Hawaii'),
                     (Idaho, 'Idaho'),
                     (Illinois, 'Illinois'),
                     (Indiana, 'Indiana'),
                     (Iowa, 'Iowa'),
                     (Kansas, 'Kansas'),
                     (Kentucky, 'Kentucky'),
                     (Louisiana, 'Louisiana'),
                     (Maine, 'Maine'),
                     (Maryland, 'Maryland'),
                     (Massachusetts, 'Massachusetts'),
                     (Michigan, 'Michigan'),
                     (Minnesota, 'Minnesota'),
                     (Mississippi, 'Mississippi'),
                     (Missouri, 'Missouri'),
                     (Montana, 'Montana'),
                     (Nebraska, 'Nebraska'),
                     (Nevada, 'Nevada'),
                     (New_Hampshire, 'New Hampshire'),
                     (New_Jersey, 'New Jersey'),
                     (New_Mexico, 'New Mexico'),
                     (New_York, 'New York'),
                     (North_Carolina, 'North Carolina'),
                     (North_Dakota, 'North Dakota'),
                     (Ohio, 'Ohio'),
                     (Oklahoma, 'Oklahoma'),
                     (Oregon, 'Oregon'),
                     (Pennsylvania, 'Pennsylvania'),
                     (Rhode_Island, 'Rhode Island'),
                     (South_Carolina, 'South Carolina'),
                     (South_Dakota, 'South Dakota'),
                     (Tennessee, 'Tennessee'),
                     (Texas, 'Texas'),
                     (Utah, 'Utah'),
                     (Vermont, 'Vermont'),
                     (Virginia, 'Virginia'),
                     (Washington, 'Washington'),
                     (West_Virginia, 'West Virginia'),
                     (Wisconsin, 'Wisconsin'),
                     (Wyoming, 'Wyoming'),
                     )
    contactid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip = models.CharField(max_length=5)
    phone = models.CharField(max_length=13)
    comments = models.TextField()

class person(models.Model):
    personid = models.AutoField(primary_key=True)
    contactid = models.ForeignKey('contact')
    name = models.CharField(max_length=45)

