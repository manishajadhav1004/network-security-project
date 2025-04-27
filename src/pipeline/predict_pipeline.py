import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("E:\\ME\\project\\Network_Security_Project", "artifacts", "model.pkl")
            preprocessor_path = os.path.join("E:\\ME\\project\\Network_Security_Project", "artifacts", "preprocessor.pkl")

            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 network_packet_size: float,
                 login_attempts: int,
                 session_duration: float,
                 ip_reputation_score: float,
                 failed_logins: int,
                 unusual_time_access: int,
                 protocol_type: str,
                 encryption_used: str,
                 browser_type: str):
        
        self.network_packet_size = network_packet_size
        self.login_attempts = login_attempts
        self.session_duration = session_duration
        self.ip_reputation_score = ip_reputation_score
        self.failed_logins = failed_logins
        self.unusual_time_access = unusual_time_access
        self.protocol_type = protocol_type
        self.encryption_used = encryption_used
        self.browser_type = browser_type

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "network_packet_size": [self.network_packet_size],
                "login_attempts": [self.login_attempts],
                "session_duration": [self.session_duration],
                "ip_reputation_score": [self.ip_reputation_score],
                "failed_logins": [self.failed_logins],
                "unusual_time_access": [self.unusual_time_access],
                "protocol_type": [self.protocol_type],
                "encryption_used": [self.encryption_used],
                "browser_type": [self.browser_type],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)