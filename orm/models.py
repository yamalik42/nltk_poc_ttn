from django.db import models


# Create your models here.
class ProjectDetail(models.Model):
    MINISTRY_CHOICES = (
        ('CFCP', 'Chemicals and Fertilizers - Chemicals and Petrochemicals'),
        ('CFF', 'Chemicals and Fertilizers - Fertilizers'),
        ('CA', 'Civil Aviation'),
        ('Co', 'Coal'),
        ('CIC', 'Commerce and Industry - Commerce'),
        ('CID', 'Commerce and Industry - DIPP'),
        ('CITT', 'Communcations and Information Technology - Telecom'),
        ('CA', 'Corporate Affairs'),
        ('Cu', 'Culture'),
        ('D', 'Defence'),
        ('DEIT', 'Department of Electronics and Information Technology'),
        ('DSEL', 'Department of School Education and Literacy'),
        ('DNER', 'Development of North Eastern Region'),
        ('EF', 'Environment and Forests'),
        ('FFS', 'Finance - Financial Services'),
        ('FFR', 'Finance - Revenue'),
        ('HFW', 'Health and Family Welfare'),
        ('HIPED', 'Heavy Industries and Pubilc Enterprises - DHI'),
        ('HA', 'Home Affairs'),
        ('MSME', 'Micro Small and Medium Enterprises'),
        ('M', 'Mines'),
        ('MES', 'Ministry of Earth Science'),
        ('MHUPA', 'Ministry of Housing and Urban Poverty Alleviation'),
        ('NRE', 'New and Renewable Energy'),
        ('PNG', 'Petroleum and Natural Gas'),
        ('P', 'Power'),
        ('R', 'Railways'),
        ('RTH', 'Road Transport and Highways'),
        ('RD', 'Rural Development'),
        ('ST', 'Science and Technology'),
        ('Sh', 'Shipping'),
        ('St', 'Steel'),
        ('Te', 'Textiles'),
        ('To', 'Tourism'),
        ('TA', 'Tribal Affairs'),
        ('UD', 'Urban Development'),
        ('WR', 'Water Resources'),
    )

    STATE_CHOICES = (
        ('ANI', 'Andaman & Nicobar UT'),
        ('AnP', 'Andhra Pradesh'),
        ('ArP', 'Arunachal Pradesh'),
        ('A', 'Assam'),
        ('B', 'Bihar'),
        ('Ch', 'Chandigarh UT'),
        ('Chh', 'Chhatisgarh'),
        ('DNH', 'Dadra and Nagar Haveli'),
        ('D', 'Daman'),
        ('D', 'Delhi'),
        ('G', 'Goa'),
        ('G', 'Gujarat'),
        ('H', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('J', 'Jharkhand'),
        ('Ka', 'Karnataka'),
        ('Ke', 'Kerala'),
        ('L', 'Lakshadweep UT'),
        ('MP', 'Madhya Pradesh'),
        ('Ma', 'Maharastra'),
        ('Man', 'Manipur'),
        ('Me', 'Meghalaya'),
        ('Mi', 'Mizoram'),
        ('N', 'Nagaland'),
        ('O', 'Odisha'),
        ('P', 'Pondicherry'),
        ('P', 'Punjab'),
        ('R', 'Rajasthan'),
        ('S', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('T', 'Telangana'),
        ('T', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('U', 'Uttarakhand'),
        ('WB', 'West Bengal'),
    )

    IMPLEMENT_MODE_CHOICES = (
        ('Pr', 'Private'),
        ('Pu', 'Public'),
        ('PPP', 'PPP'),
    )


    project_name = models.CharField(max_length=42)
    sponsoring_ministry = models.CharField(max_length=6, choices=MINISTRY_CHOICES)
    location_one = models.CharField(max_length=4, choices=STATE_CHOICES)
    location_two = models.CharField(max_length=4, choices=STATE_CHOICES, blank=True)
    location_three = models.CharField(max_length=4, choices=STATE_CHOICES, blank=True)
    implementation_mode = models.CharField(max_length=3, choices=IMPLEMENT_MODE_CHOICES)
    project_cost = models.PositiveIntegerField()
    project_description = models.TextField(max_length=442)
