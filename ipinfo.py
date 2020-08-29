#!/usr/bin/env python3

import geoip2.database

def GetReader(type):
	if type == 'city':
		mmdb = geoip2.database.Reader('dbs/GeoLite2-City.mmdb')
		return mmdb
	if type == 'asn':
		mmdb = geoip2.database.Reader('dbs/GeoLite2-Asn.mmdb')
		return mmdb
	return None

def GetIpInfo(ip):
	city, country, lat, lon = GetLocation(ip)
	ipInfo = { 'ip': ip, 'city': city, 'country': country, 'lat': lat, 'lon': lon }
	PrintIpInfo(ipInfo)

def GetLocation(ip):
	mmdb = GetReader('city')
	if mmdb == None:
		print('[!] Error: No valid mmdb reader was created.')
		exit()
	cityInfo = mmdb.city(ip)
	mmdb.close()
	return cityInfo.city.name, cityInfo.country.name, cityInfo.location.latitude, cityInfo.location.longitude

def PrintIpInfo(ipInfo):
	print('IP: {}'.format(ipInfo['ip']))
	print('City: {}'.format(ipInfo['city']))
	print('Country: {}'.format(ipInfo['country']))
	print('Latitude: {}'.format(ipInfo['lat']))
	print('Longitude: {}'.format(ipInfo['lon']))

ip = input('Enter IP: ')

GetIpInfo(ip)
