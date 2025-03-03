# Project Based ROTC (Spring 2025)


This is the repository for the project based rotc. We will be working to build a predictor for Traumatic Brain Injury (TBI) using the [MIMIC-IV dataset](https://physionet.org/content/mimiciv/3.1/).

## Downloading the data
We will be working with the [`hosp`](https://physionet.org/content/mimiciv/3.1/hosp/#files-panel) data, which contains information about hospitalizations for 223,452 patients. Please download the file here into the data directory within the repo.
You can do this using the following command:

```bash
# First, ensure you have credentials set up for PhysioNet
# You need to register at https://physionet.org and gain access to MIMIC-IV

# Create data directory if it doesn't exist
mkdir -p data

# Download MIMIC-IV hospital data (requires PhysioNet credentials)
wget -r -N -c -np --user=YOUR_PHYSIONET_USERNAME --ask-password \
  https://physionet.org/files/mimiciv/3.1/hosp/ \
  -P data/

# YOUR_PHYSIONET_USERNAME is your PhysioNet usename and you will be prompted to provide your password.