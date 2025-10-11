# your_app/daily_utils.py
import time
from django.conf import settings
from daily import Daily

# Initialize the Daily client once
Daily.init(settings.DAILY_API_KEY)

def create_daily_meeting_for_appointment(appointment):
    """
    Creates a Daily.co room for a specific appointment.
    
    - Sets auto-start for audio-only recording.
    - Uses the appointment's ID in the room name for easy tracking.
    """
    try:
        # Create a unique, predictable room name
        room_name = f"appointment-{appointment.id}-{int(time.time())}"

        # Define room properties
        properties = {
            'properties': {
                'exp': time.time() + (7 * 24 * 3600),  # Room expires in 7 days
                
                # --- This is the key for automatic recording ---
                'start_cloud_recording': True, # Automatically start recording when first person joins
                'recording_mode': 'cloud',
                'recording_options': {
                    'layout': {
                        'preset': 'custom',
                        'composition': 'audio-only'
                    }
                }
            }
        }
        
        room_info = Daily.create_room(name=room_name, properties=properties)

        if room_info and 'url' in room_info:
            # Return both the URL and the name for saving
            return room_info.get('url'), room_info.get('name')
        
        return None, None

    except Exception as e:
        print(f"Error creating Daily.co room: {e}") # Replace with proper logging
        return None, None