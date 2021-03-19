import logging
import json

from scraper.components import *

#https://coralogix.com/log-analytics-blog/python-logging-best-practices-tips/#id.1ksv4uv
#https://gist.github.com/nguyenkims/e92df0f8bd49973f0c94bddf36ed7fd0
#https://towardsdatascience.com/get-your-own-data-building-a-scalable-web-scraper-with-aws-654feb9fdad7
formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
streamhandler = logging.StreamHandler()
streamhandler.setFormatter(formatter)
logger.addHandler(streamhandler)



class Scraper:
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.table = get_table('JobTable')
    
    def start(self, queries, **kwargs):
        """Start Scraping the website"""
        
        logger.info('Scraper started')
        
        # fetch all jobs using Multithreading and process using Multiprocessing based on queries 
        jobs = Utils.fetch_jobs(self.base_url, queries)
        
        # save into dynamoDB
        db.save(self.table, jobs)
   
        logger.info('scraping done')
        
        response = {
            "statusCode": 200,
            "body": json.dumps({'message':'Successfully scraped.'})
        }
        
        return response