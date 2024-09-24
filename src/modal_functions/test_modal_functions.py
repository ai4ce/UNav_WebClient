import base64
import os

import modal


def main():

    UnavServer = modal.Cls.lookup("unav-server", "UnavServer")
    unav_server = UnavServer()
    current_directory = os.getcwd()
    full_image_path = os.path.join(
        current_directory, "modal_functions/misc/sample2.png"
    )

    # with open(full_image_path, "rb") as image_file:
    #     image_data = image_file.read()
    #     base64_encoded = base64.b64encode(image_data).decode("utf-8")
    # print(unav_server.localize.remote(base64_encoded))
    # print(unav_server.get_destinations_list.remote())
    destination_id = "07993"
    print(unav_server.select_user_destination.remote(destination_id))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")