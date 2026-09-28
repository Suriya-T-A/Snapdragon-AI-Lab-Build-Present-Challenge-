# SnapStudy AI

Privacy-first, on-device study assistant concept for Snapdragon-powered PCs.

## Included baseline
- Extractive summary from pasted plain-text notes
- Simple fill-in-the-blank revision prompts
- Standard-library Python only; no network calls

**Important:** This baseline does not yet include a generative AI model or Snapdragon-specific acceleration. Those are planned integration and validation steps, not completed features.

## Run
Requires Python 3.10+.

```bash
python main.py
```
Paste notes, then type `END` on a new line.

## Planned next steps
1. Add a local open-source instruction model through a compatible local inference runtime.
2. Check model license, memory requirements, and ARM64/Windows compatibility.
3. Evaluate Qualcomm AI Hub or other supported Snapdragon deployment options.
4. Test on the participant's Snapdragon-powered HP PC and publish measured latency, memory use, and offline behavior.
5. Add a user interface and document reproducible setup.

## Submission checklist
- Confirm eligibility and laptop requirement against the official rules.
- Run and test the prototype on your own device.
- Make meaningful participant-owned improvements before submission.
- Replace planned/future statements with verified results only.
- Do not upload confidential notes, credentials, or third-party material without permission.
