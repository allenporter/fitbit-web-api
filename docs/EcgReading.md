# EcgReading

## Properties

| Name                           | Type          | Description                                                                                                            | Notes      |
| ------------------------------ | ------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------- |
| **start_time**                 | **datetime**  | The date and time when the reading was started on the device.                                                          | [optional] |
| **average_heart_rate**         | **int**       | The average heart rate of the user during the reading.                                                                 | [optional] |
| **result_classification**      | **str**       | The classification of the ECG result.                                                                                  | [optional] |
| **waveform_samples**           | **List[int]** | An array of integers representing the ECG waveform.                                                                    | [optional] |
| **sampling_frequency_hz**      | **int**       | The frequency in hertz at which the Fitbit ECG app sampled the voltage.                                                | [optional] |
| **scaling_factor**             | **int**       | The scaling factor used to convert waveform samples to ECG voltages in mV (mV &#x3D; waveformSamples / scalingFactor). | [optional] |
| **number_of_waveform_samples** | **int**       | The total number of samples in the reading.                                                                            | [optional] |
| **lead_number**                | **int**       | The ECG lead being used to take the reading.                                                                           | [optional] |
| **feature_version**            | **str**       | The version of the ECG app running on the device.                                                                      | [optional] |
| **device_name**                | **str**       | Hardware name of the compatible wrist-worn device used to take the reading.                                            | [optional] |
| **firmware_version**           | **str**       | Firmware running on the compatible wrist-worn device used to take the reading.                                         | [optional] |

## Example

```python
from fitbit_web_api.models.ecg_reading import EcgReading

# TODO update the JSON string below
json = "{}"
# create an instance of EcgReading from a JSON string
ecg_reading_instance = EcgReading.from_json(json)
# print the JSON string representation of the object
print(EcgReading.to_json())

# convert the object into a dict
ecg_reading_dict = ecg_reading_instance.to_dict()
# create an instance of EcgReading from a dict
ecg_reading_from_dict = EcgReading.from_dict(ecg_reading_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
