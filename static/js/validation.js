function addRow() {
    var table = document.getElementById("itemsTable").getElementsByTagName('tbody')[0];
    var row = table.insertRow();
    row.className = "item-row";
    row.innerHTML = `
        <td>
            <input type="text" name="item_name[]" class="form-control mb-2" placeholder="Item Name" required>
            <div class="row g-1 small-inputs">
                <div class="col-6"><input type="text" name="glass_type[]" class="form-control form-control-sm" placeholder="Glass Type"></div>
                <div class="col-6"><input type="text" name="frame_color[]" class="form-control form-control-sm" placeholder="Frame Color"></div>
                <div class="col-6"><input type="text" name="mosquito_net[]" class="form-control form-control-sm" placeholder="Mosquito Net"></div>
                <div class="col-6"><input type="text" name="accessories[]" class="form-control form-control-sm" placeholder="Accessories"></div>
                <div class="col-12"><input type="text" name="jobs[]" class="form-control form-control-sm" placeholder="Jobs/Services"></div>
            </div>
        </td>
        <td><input type="number" step="0.1" name="width[]" class="form-control width" value="0" oninput="calculateRow(this)"></td>
        <td><input type="number" step="0.1" name="height[]" class="form-control height" value="0" oninput="calculateRow(this)"></td>
        <td><input type="number" name="palla[]" class="form-control palla" value="1" min="1" oninput="calculateRow(this)"></td>
        <td><input type="number" name="h_lines[]" class="form-control" value="0"></td>
        <td><input type="number" name="v_lines[]" class="form-control" value="0"></td>
        <td>
            <select name="lock_system[]" class="form-select form-select-sm">
                <option value="Central Mortise Lock">Central Mortise Lock</option>
                <option value="Touch Lock">Touch Lock</option>
                <option value="No Lock">No Lock</option>
            </select>
        </td>
        <td><input type="number" name="rate[]" class="form-control rate" value="0" oninput="calculateRow(this)"></td>
        <input type="hidden" class="row-total" value="0">
        <td class="text-center"><button type="button" class="btn btn-danger btn-sm" onclick="this.closest('tr').remove(); calculateGrandTotal();">Remove</button></td>
    `;
}

function calculateRow(input) {
    var row = input.closest('tr');
    var width = parseFloat(row.querySelector('.width').value) || 0;
    var height = parseFloat(row.querySelector('.height').value) || 0;
    var rate = parseFloat(row.querySelector('.rate').value) || 0;
    
    var area = width * height;
    row.querySelector('.row-total').value = area * rate;
    calculateGrandTotal();
}

function calculateGrandTotal() {
    var totals = document.querySelectorAll('.row-total');
    var subtotal = 0;
    totals.forEach(function(t) { subtotal += parseFloat(t.value) || 0; });
    
    var gstRate = parseFloat(document.getElementById('gstRateInput').value) || 0;
    var gst = subtotal * (gstRate / 100);
    
    document.getElementById('summarySubtotal').innerText = "₹" + subtotal.toFixed(2);
    document.getElementById('summaryGST').innerText = "₹" + gst.toFixed(2);
    document.getElementById('summaryGrandTotal').innerText = "₹" + (subtotal + gst).toFixed(2);
}

document.addEventListener("DOMContentLoaded", calculateGrandTotal);