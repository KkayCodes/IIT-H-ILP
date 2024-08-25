import matplotlib.pyplot as plt
import numpy as np

# Data without preprocessing
files_no_pp = [
    "nonemb_gt", "sansk_gt", "sc2_gt", "simple_gt", "skew_gt",
    "t1_gt", "t2_gt", "t3_gt", "t4_gt", "t5.gt", "t6_gt", "t7_gt"
]
cer_no_pp = [0.8958, 3.4025, 0.6392, 0.1951, 0.9183, 0.1522, 0.6818, 0.9612, 0.8184, 0.8038, 0.5151, 0.2622]
wer_no_pp = [7.6693, 30.0000, 31.0000, 3.2000, 39.9091, 9.3333, 27.0000, 59.5000, 44.1250, 31.6250, 9.8889, 10.5294]

# Data with preprocessing
files_pp = [
    "nonemb_gt", "sansk_gt", "sc2_gt", "simple_gt", "skew_gt",
    "t1_gt", "t2_gt", "t3_gt", "t4_gt", "t5.gt", "t6_gt", "t7_gt"
]
cer_pp = [0.8702, 0.7862, 0.6211, 0.1951, 0.8501, 0.1793, 0.3719, 0.9564, 0.8414, 0.8133, 0.6055, 0.3265]
wer_pp = [7.4488, 6.8333, 30.1250, 3.0000, 36.9091, 11.0000, 15.0000, 59.0500, 45.2500, 31.8750, 11.7222, 13.2353]

# Create plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# CER Plot
x = np.arange(len(files_no_pp))
width = 0.35  # width of the bars

ax1.bar(x - width/2, np.array(cer_no_pp) * 100, width, label='No Preprocessing', color='blue')
ax1.bar(x + width/2, np.array(cer_pp) * 100, width, label='Preprocessing', color='orange')

ax1.set_xlabel('File')
ax1.set_ylabel('CER (%)')
ax1.set_title('Character Error Rate (CER) Comparison')
ax1.set_xticks(x)
ax1.set_xticklabels([f"{file}_out" for file in files_no_pp], rotation=90)
ax1.legend()

# WER Plot
ax2.bar(x - width/2, wer_no_pp, width, label='No Preprocessing', color='blue')
ax2.bar(x + width/2, wer_pp, width, label='Preprocessing', color='orange')

ax2.set_xlabel('File')
ax2.set_ylabel('WER')
ax2.set_title('Word Error Rate (WER) Comparison')
ax2.set_xticks(x)
ax2.set_xticklabels([f"{file}_out" for file in files_no_pp], rotation=90)
ax2.legend()

# Adjust layout
plt.tight_layout()
plt.show()

plt.savefig('san.png')
