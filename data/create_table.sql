Begin Transaction;
Create  TABLE MAIN.COUNTY_PROVINCE_LINK(
[county] text PRIMARY KEY,
[province] text,
[country] text
) ;

Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Dublin', 'Leinster');
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Wicklow', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Carlow', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Kildare', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Wexford', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Westmeath', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Offaly', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country])  
values ('Meath', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country])  
values ('Louth', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Longford', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Laois', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Kilkenny', 'Leinster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Antrim', 'Ulster', 'UK'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Armagh', 'Ulster', 'UK'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Cavan', 'Ulster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Donegal', 'Ulster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Down', 'Ulster', 'UK'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Fermanagh', 'Ulster', 'UK'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Londonderry', 'Ulster', 'UK'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Monaghan', 'Ulster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Tyrone', 'Ulster', 'UK'); 

Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Clare', 'Munster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Cork', 'Munster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Kerry', 'Munster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Limerick', 'Munster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Tipperary', 'Munster', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Waterford', 'Munster', 'ROI'); 

Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Galway', 'Connacht', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Leitrim', 'Connacht', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Mayo', 'Connacht', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Roscommon', 'Connacht', 'ROI'); 
Insert Into MAIN.[COUNTY_PROVINCE_LINK] ([county],[province],[country]) 
values ('Sligo', 'Connacht', 'ROI'); 
   
Commit Transaction;