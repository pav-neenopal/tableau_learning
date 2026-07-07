import os
import json
import requests
import tableauserverclient as TSC

# -------------------------------------------------------
# GitHub Secrets
# -------------------------------------------------------

SERVER_URL = os.environ["TABLEAU_SERVER"]
SITE_NAME = os.environ["TABLEAU_SITE"]
PAT_NAME = os.environ["TABLEAU_PAT_NAME"]
PAT_SECRET = os.environ["TABLEAU_PAT_SECRET"]

WORKBOOK_NAME = "Sales Dashboard"
WORKBOOK_PATH = "Sales Dashboard.twbx"
PROJECT_NAME = "default"

# -------------------------------------------------------
# Login
# -------------------------------------------------------

tableau_auth = TSC.PersonalAccessTokenAuth(
    PAT_NAME,
    PAT_SECRET,
    SITE_NAME
)

server = TSC.Server(SERVER_URL, use_server_version=True)

with server.auth.sign_in(tableau_auth):

    auth_token = server.auth_token
    site_id = server.site_id

    headers = {
        "X-Tableau-Auth": auth_token
    }

    # -------------------------------------------------------
    # Find Project
    # -------------------------------------------------------

    projects, _ = server.projects.get()

    project = next(
        (p for p in projects if p.name == PROJECT_NAME),
        None
    )

    if project is None:
        raise Exception(f"Project '{PROJECT_NAME}' not found.")

    # -------------------------------------------------------
    # Find Existing Workbook
    # -------------------------------------------------------

    workbooks, _ = server.workbooks.get()

    existing = next(
        (
            wb for wb in workbooks
            if wb.name == WORKBOOK_NAME
        ),
        None
    )

    # -------------------------------------------------------
    # Save BEFORE permissions
    # -------------------------------------------------------

    if existing:

        print("Workbook already exists.")

        permission_url = (
            f"{SERVER_URL}/api/{server.version}/sites/"
            f"{site_id}/workbooks/{existing.id}/permissions"
        )

        response = requests.get(
            permission_url,
            headers=headers
        )

        if response.status_code == 200:

            with open(
                "permissions_before.json",
                "w",
                encoding="utf-8"
            ) as f:

                try:
                    json.dump(
                        response.json(),
                        f,
                        indent=4
                    )
                except Exception:
                    f.write(response.text)

            print("permissions_before.json saved.")

        else:

            print(
                "Could not fetch permissions before deployment:"
            )
            print(response.text)

    else:

        print(
            "Workbook does not exist. Skipping before snapshot."
        )

    # -------------------------------------------------------
    # Publish Workbook
    # -------------------------------------------------------

    workbook_item = TSC.WorkbookItem(project.id)

    new_workbook = server.workbooks.publish(
        workbook_item,
        WORKBOOK_PATH,
        TSC.Server.PublishMode.Overwrite
    )

    print(f"Workbook published: {new_workbook.name}")

    # -------------------------------------------------------
    # Save AFTER permissions
    # -------------------------------------------------------

    permission_url = (
        f"{SERVER_URL}/api/{server.version}/sites/"
        f"{site_id}/workbooks/{new_workbook.id}/permissions"
    )

    response = requests.get(
        permission_url,
        headers=headers
    )

    if response.status_code == 200:

        with open(
            "permissions_after.json",
            "w",
            encoding="utf-8"
        ) as f:

            try:
                json.dump(
                    response.json(),
                    f,
                    indent=4
                )
            except Exception:
                f.write(response.text)

        print("permissions_after.json saved.")

    else:

        print(
            "Could not fetch permissions after deployment:"
        )
        print(response.text)

print("Deployment completed successfully.")
