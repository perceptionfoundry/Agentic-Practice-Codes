#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from stock_picker.crew import StockPredictor

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the research crew.
    """
    # Check for required environment variables
    if not os.getenv('SERPER_API_KEY'):
        print("Warning: SERPER_API_KEY environment variable not set")
    
    inputs = {
        'sector': 'Technology',
        "current_date": str(datetime.now())
    }

    try:
        # Create and run the crew
        result = StockPredictor().crew().kickoff(inputs=inputs)

        # Print the result
        print("\n\n=== FINAL DECISION ===\n\n")
        print(result.raw)
        
        # If you want to access the pydantic output
        if hasattr(result, 'pydantic'):
            print("\n\n=== STRUCTURED OUTPUT ===\n\n")
            print(result.pydantic)
            
    except Exception as e:
        print(f"Error running crew: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run()