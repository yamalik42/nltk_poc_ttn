# Generated by Django 2.2 on 2019-04-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_auto_20190425_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='location_three',
            field=models.CharField(blank=True, choices=[('ANI', 'Andaman & Nicobar UT'), ('AnP', 'Andhra Pradesh'), ('ArP', 'Arunachal Pradesh'), ('A', 'Assam'), ('B', 'Bihar'), ('Ch', 'Chandigarh UT'), ('Chh', 'Chhatisgarh'), ('DNH', 'Dadra and Nagar Haveli'), ('D', 'Daman'), ('D', 'Delhi'), ('G', 'Goa'), ('G', 'Gujarat'), ('H', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('J', 'Jharkhand'), ('Ka', 'Karnataka'), ('Ke', 'Kerala'), ('L', 'Lakshadweep UT'), ('MP', 'Madhya Pradesh'), ('Ma', 'Maharastra'), ('Man', 'Manipur'), ('Me', 'Meghalaya'), ('Mi', 'Mizoram'), ('N', 'Nagaland'), ('O', 'Odisha'), ('P', 'Pondicherry'), ('P', 'Punjab'), ('R', 'Rajasthan'), ('S', 'Sikkim'), ('TN', 'Tamil Nadu'), ('T', 'Telangana'), ('T', 'Tripura'), ('UP', 'Uttar Pradesh'), ('U', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=4),
        ),
        migrations.AlterField(
            model_name='projectdetail',
            name='location_two',
            field=models.CharField(blank=True, choices=[('ANI', 'Andaman & Nicobar UT'), ('AnP', 'Andhra Pradesh'), ('ArP', 'Arunachal Pradesh'), ('A', 'Assam'), ('B', 'Bihar'), ('Ch', 'Chandigarh UT'), ('Chh', 'Chhatisgarh'), ('DNH', 'Dadra and Nagar Haveli'), ('D', 'Daman'), ('D', 'Delhi'), ('G', 'Goa'), ('G', 'Gujarat'), ('H', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('J', 'Jharkhand'), ('Ka', 'Karnataka'), ('Ke', 'Kerala'), ('L', 'Lakshadweep UT'), ('MP', 'Madhya Pradesh'), ('Ma', 'Maharastra'), ('Man', 'Manipur'), ('Me', 'Meghalaya'), ('Mi', 'Mizoram'), ('N', 'Nagaland'), ('O', 'Odisha'), ('P', 'Pondicherry'), ('P', 'Punjab'), ('R', 'Rajasthan'), ('S', 'Sikkim'), ('TN', 'Tamil Nadu'), ('T', 'Telangana'), ('T', 'Tripura'), ('UP', 'Uttar Pradesh'), ('U', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=4),
        ),
    ]
