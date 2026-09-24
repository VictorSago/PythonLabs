
# ==========================================================
# Part H - Applied challenge: Export system
# ==========================================================

# 1. Build a small export system using the concepts from today's lesson.
# 2. Create a base class Exporter with a method export(data).
# 5. Add a useful __str__ method to the exporter classes.
class Exporter:
    def export(self, data):
        return f"Exporting data: {data}"

    def __str__(self):
        return f"{type(self).__name__} exporter"


# 3. Create at least three subclasses, for example ConsoleExporter, TextExporter and SummaryExporter.
# 4. Override export(data) in every subclass so each handles the same data differently.
class ConsoleExporter(Exporter):
    def export(self, data):
        return f"[Console] {data}"

    def __str__(self):
        return super().__str__() + " (inherits Exporter)"


class TextExporter(Exporter):
    def export(self, data):
        return f"Writing to text format:\n{data}"

    def __str__(self):
        return super().__str__() + " (inherits Exporter)"


class SummaryExporter(Exporter):
    def export(self, data):
        if isinstance(data, (list, tuple)):
            return f"Summary: {len(data)} item(s) exported."
        return "Summary: 1 item exported."

    def __str__(self):
        return super().__str__() + " (inherits Exporter)"


# 6. Create several exporter objects and store them in one list.
sample_data = ["Order #1001", "Order #1002", "Order #1003"]
exporters = [ConsoleExporter(), TextExporter(), SummaryExporter()]

# 7. Loop through the list and call export() on each object to
# demonstrate polymorphism.
for exporter in exporters:
    print(f"--- {exporter} ---")
    print(exporter.export(sample_data))

# 8. Create one additional class that is not part of the Exporter inheritance
# hierarchy but still provides an export(data) method. Show that it can be
# used by the same calling code.
class JSONExporter:
    def export(self, data):
        return f'{{"data": {data!r}}}'

    def __str__(self):
        return "JSON Exporter"


new_exporter = JSONExporter()
exporters.append(new_exporter)
for exporter in exporters:
    print(f"--- {exporter} ---")
    print(exporter.export(sample_data))

# 9. Use isinstance() at least once to inspect a meaningful type relationship.
console_exporter, text_exporter, summary_exporter, json_exporter = exporters

print("console_exporter is an Exporter:", isinstance(console_exporter, Exporter))
print("json_exporter is an Exporter:", isinstance(json_exporter, Exporter))
# JSONExporter has an export() method and works fine in the loop above, but it
# never inherited from Exporter, so isinstance() correctly reports it isn't one.


# 10. Add one example of composition to the program and explain the HAS-A relationship in a comment.
class ExportManager:
    def __init__(self, exporter):
        self.exporter = exporter  # composition: ExportManager HAS-A exporter

    def run_export(self, data):
        return self.exporter.export(data)


manager_1 = ExportManager(console_exporter)
manager_2 = ExportManager(json_exporter)

print(manager_1.run_export(sample_data))
print(manager_2.run_export(sample_data))

# ExportManager HAS-A exporter, not IS-A exporter: it stores whichever exporter
# object it was given and delegates the actual work to it, rather than being a
# kind of exporter itself. Because of that, run_export() works with any object
# that has an export() method - an Exporter subclass or, as shown with
# manager_2, JSONExporter, which isn't part of that hierarchy at all.
