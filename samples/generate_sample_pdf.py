"""Generates a sample oil & gas equipment manual PDF for testing the RAG app."""

from fpdf import FPDF


def add_page(pdf: FPDF, heading: str, body: str):
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.multi_cell(0, 10, heading)
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 12)
    pdf.multi_cell(0, 7, body)


pdf = FPDF()

add_page(
    pdf,
    "XR-200 Centrifugal Pump - Equipment Overview",
    "The XR-200 is a horizontal centrifugal pump used for transferring produced water and "
    "light crude in upstream field operations. Rated flow: 450 GPM at 150 ft head. "
    "Maximum operating pressure: 275 PSI. Maximum fluid temperature: 180 F. "
    "The unit consists of a cast steel volute casing, a single-stage enclosed impeller, "
    "a mechanical shaft seal, and an API 610 compliant baseplate. "
    "Motor: 75 HP, 3-phase, 460V, driven through a flexible coupling.",
)

add_page(
    pdf,
    "Section 4: Mechanical Seal Replacement Procedure",
    "Tools required: 10mm and 13mm socket set, seal puller, torque wrench, clean rags, "
    "replacement mechanical seal kit (part no. XR200-MS-14).\n\n"
    "Step 1: Isolate the pump from the system by closing the suction and discharge valves. "
    "Relieve all residual system pressure through the vent valve before proceeding.\n\n"
    "Step 2: Lock out and tag out the motor power supply per site LOTO procedure.\n\n"
    "Step 3: Remove the coupling guard and disconnect the coupling.\n\n"
    "Step 4: Remove the seal housing bolts (8x M10) and slide the housing back along the shaft.\n\n"
    "Step 5: Extract the old mechanical seal using the seal puller. Inspect the shaft sleeve "
    "for scoring or wear; replace the sleeve if wear exceeds 0.5mm.\n\n"
    "Step 6: Clean the shaft and seal seat thoroughly with a lint-free cloth. Do not use "
    "abrasive materials on the seal seat surface.\n\n"
    "Step 7: Install the new mechanical seal with the spring facing the impeller. Lubricate "
    "the shaft lightly with glycerin before sliding the seal into place.\n\n"
    "Step 8: Reinstall the seal housing and torque the housing bolts to 35 Nm in a criss-cross "
    "pattern.\n\n"
    "Step 9: Reconnect the coupling, reinstall the guard, remove lockout, and perform a slow-roll "
    "test before returning the pump to full operating pressure.",
)

add_page(
    pdf,
    "Section 7: Troubleshooting Guide",
    "Symptom: Pump is leaking at the seal.\n"
    "Likely cause: Worn or improperly seated mechanical seal, or a scored shaft sleeve.\n"
    "Recommended action: Shut down the pump, follow the seal replacement procedure in "
    "Section 4. Inspect the shaft sleeve for wear during replacement.\n\n"
    "Symptom: Pump is cavitating (loud rattling noise, unstable discharge pressure).\n"
    "Likely cause: Insufficient suction pressure (NPSH), clogged suction strainer, or air "
    "ingress at the suction line.\n"
    "Recommended action: Check suction strainer for blockage, verify suction valve is fully "
    "open, and inspect suction piping for air leaks. Do not run the pump dry.\n\n"
    "Symptom: Motor trips on overload shortly after start-up.\n"
    "Likely cause: Discharge valve closed on start-up, bearing failure, or impeller binding.\n"
    "Recommended action: Confirm discharge valve is open before start-up. If the trip persists "
    "with the valve open, shut down and inspect bearings and impeller clearance.\n\n"
    "All troubleshooting steps involving disassembly, electrical isolation, or pressurized "
    "components must be verified by qualified maintenance personnel before execution.",
)

add_page(
    pdf,
    "Section 9: Routine Maintenance Schedule",
    "Daily: Visually inspect for leaks at the seal and flanges. Check discharge pressure "
    "gauge against baseline.\n\n"
    "Weekly: Check motor and bearing temperatures with an infrared thermometer. Log vibration "
    "readings if a handheld vibration meter is available.\n\n"
    "Monthly: Grease bearings per the lubrication chart (Section 10). Inspect coupling "
    "alignment and coupling element wear.\n\n"
    "Every 6 months: Replace mechanical seal if vibration or minor weeping has been logged, "
    "even if not yet leaking. Inspect baseplate grouting for cracks.\n\n"
    "Annually: Full pump teardown and inspection, including impeller wear ring clearance "
    "measurement and shaft runout check.\n\n"
    "All maintenance recommendations in this manual are general guidance only and must be "
    "verified against site-specific procedures by qualified personnel before being carried out.",
)

pdf.output("samples/XR-200_Pump_Manual.pdf")
print("Written: samples/XR-200_Pump_Manual.pdf")
