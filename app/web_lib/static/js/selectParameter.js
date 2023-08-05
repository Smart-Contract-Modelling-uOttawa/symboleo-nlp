OPTIONS_DICT = {

}


// Add new text value to the running input 
function updateRunningValue(value) {
  var $inputContainer = $('#running-input-value');
  currText = $inputContainer.text()

  newText = currText + ' ' + value
  $inputContainer.text(newText);

  // var $span = $('<span>').text(value);
  //   $span.addClass('input-value');
  //   $inputContainer.text(newText);
}

// Process a value entered by the user
function processValue(input_id, value) {
  // Hide things
  // $('#unit-selection-container').hide()
  $('#option-selection-container').hide();
  $('#value-entry-container').hide();
  $('#input-value-form').val('')
  OPTIONS_DICT = {}
  $('#option-selection').empty();



  // Send the AJAX request
  $.ajax({
    url: '/value',
    method: 'POST',
    data: {
      input_id: input_id,
      value: value
    },
    success: function(response) {
      presentUnits(response.units)
    },
    error: function(error) {
      console.error('Error updating content:', error);
    }
  });
}


function submitDynamicValue() { 
  var input_id = $('#input-value-label').attr('data-input-id');
  var value = $('#input-value-form').val();

  updateRunningValue(value)
  processValue(input_id, value)
}



function getUnitClass(unit_variety) {
  if (unit_variety == 'EMPTY') {
    return 'btn-outline-secondary'
  }
  
  if (unit_variety == 'STATIC') {
    return 'btn-outline-primary'
  }

  return 'btn-outline-success'
}

// When user selects value from options dropdown
function selectDynamicValue() {
  // Get the type
  var input_id = $('#select-value-label').text(); 

  // Get the value
  var selected_value = $('#option-selection').val();

  // Update and process
  updateRunningValue(selected_value)
  processValue(input_id, selected_value)
}


function fillDynamicOptions(input_id, options) {
  // get the select
  var $selectElement = $("#option-selection");

  // Fill the label
  $('#select-value-label').text(input_id);

  // Populate
  $.each(options, function(index, x) {
    var next_option = $("<option>", { text: x });
    $selectElement.append(next_option);
  }); 

    // Show the container
  $("#option-selection-container").show()  
}

// Prep for user inputting a dynamic value
function setupDynamicValue(input_id, prompt) {
  // Fetch the options
  options = OPTIONS_DICT[input_id]

  // Fill options
  if (options && options.length > 0) {
    fillDynamicOptions(input_id, options)
  }

  $('#value-entry-container').show();
  $('#input-value-label').attr('data-input-id', input_id);
  $('#input-value-label').text(prompt);  
}

// User selects an input type
function handleInputClick(unit) {
  input_id = unit.unit_type

  if (unit.variety == 'EMPTY') {
    processValue(input_id, null)
  } else if (unit.variety == 'STATIC') {
    // Static unit
    updateRunningValue(unit.default_value)
    processValue(input_id, unit.default_value)    
  } else {
    // Dynamic unit
    setupDynamicValue(input_id, unit.prompt)
  }
}


// Fill the selection grid with valid units
function presentUnits(units) {
  var $selectionGrid = $('#unit-selection-grid');

  // Clear the existing buttons
  $selectionGrid.empty();

  // Store units in a dict for later
  unit_keys = Object.keys(units)
  unit_keys.forEach(k => {
    unit = units[k]
    OPTIONS_DICT[unit.unit_type] = unit.options
  })

  // Use final node to display the submission
  // OR if no children present
  // But filter it out from presentation
  if (unit_keys.includes('FINAL_NODE') || unit_keys.length == 0) {
    $('#parameter-submission-container').show()
  }
  filtered_keys = unit_keys.filter(x => x !== 'FINAL_NODE');

  // Iterate through the strings and create buttons
  // Each button needs a further handler
  $.each(filtered_keys, function(index, k) {
    unit = units[k]

    var button = $('<button>').text(unit.prompt);
    unit_class = getUnitClass(unit.variety)
    button.addClass('btn').addClass('btn-sm').addClass('unit-button').addClass(unit_class)
    
    $selectionGrid.append(button);

    (function(b_unit) {
        button.click(function() {
          handleInputClick(b_unit);
        });
    })(unit);

    // button.click(function() {
    //   handleInputClick(unit);
    // });
    
  });   
  
  // Show the container
  $('#unit-selection-container').show()
}

// User chooses a parameter
// Fetch the initial units and present to user
function selectParameter() {
  var selectedParm = $('#parm-selection').val();

  // Will want to clear some things
  $('#running-input-container').show()
  // clear the running input
  // ...

  $.ajax({
    url: '/parameter',
    method: 'POST',
    data: {
      parameter: selectedParm
    },
    success: function(response) {
      presentUnits(response.units)
    },
    error: function(error) {
      console.error('Error updating content:', error);
    }
  });
}

// Start
$( document ).ready(function() {
  $('#unit-selection-container').hide()
  $('#option-selection-container').hide();
  $('#value-entry-container').hide();
  $('#running-input-container').hide()
  $('#parameter-submission-container').hide()
  
});