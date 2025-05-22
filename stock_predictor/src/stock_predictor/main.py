#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from stock_predictor.crew import StockPredictor

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the research crew. Run the stock picker crew.
    """
    
    inputs = {
        'ctor': 'Energy',
        "current_date": str(datetime.now())
    }
    
    result = StockPredictor().crew().kickoff(input=inputs)
    
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)
    
    
if __name__ == '__main__':
    run()