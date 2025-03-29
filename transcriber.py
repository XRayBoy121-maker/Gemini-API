import speech_recognition as sr
import time # Optional: For slight pauses if needed

def transcribe_from_microphone(timeout_seconds=5):
    """
    Listens to the default microphone, transcribes the speech to text,
    and returns the transcribed text or None if transcription fails.

    Args:
        timeout_seconds (int): Max seconds to wait for speech to start.
        phrase_time_limit_seconds (int): Max seconds to record after speech starts.

    Returns:
        str or None: The transcribed text, or None if an error occurred.
    """
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        # Listen for 1 second to adjust the energy threshold based on ambient noise level
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(f"\nOkay, speak now!")
        print(f"(Waiting up to {timeout_seconds}s for speech to start )")

        try:
            # Listen for the first phrase and extract it into audio data
            # timeout: seconds to wait for phrase to start before giving up (WaitTimeoutError)
            # phrase_time_limit: max seconds that phrase is allowed to be recorded
            audio_data = recognizer.listen(source, timeout=timeout_seconds)
            print("Got it! Processing audio...")

            # Recognize speech using Google Web Speech API
            # This requires an internet connection
            text = recognizer.recognize_google(audio_data)
            print(f"\nTranscription: {text}")
            return text

        except sr.WaitTimeoutError:
            print(f"\nError: No speech detected within {timeout_seconds} seconds.")
            return None
        except sr.UnknownValueError:
            print("\nError: Google Speech Recognition could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"\nError: Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            return None

# --- Main execution ---
if __name__ == "__main__":
    transcribed_text = transcribe_from_microphone()

    if transcribed_text:
        print("\nSuccessfully transcribed.")
        # You could add code here to DO something with the transcribed_text
        # e.g., pass it to another function, save it, etc.
    else:
        print("\nTranscription failed.")