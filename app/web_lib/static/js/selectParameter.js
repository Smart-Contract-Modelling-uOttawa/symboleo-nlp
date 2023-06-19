EMPTY_VAL = '[EMPTY]'

input_value_dict = {
  'WITHIN': 'within',
  'IF': 'if',
  'BEFORE': 'before',
  'AFTER': 'after',
  'OF': 'of',
  'UNLESS': 'unless',
  'EVENT': EMPTY_VAL,
  'CUSTOM_EVENT': EMPTY_VAL,
  'NORM_EVENT': EMPTY_VAL,
  'SUBJECT': null,
  'VERB': null,
  'DATE': null,
  'TIMESPAN': null
  //....
}

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
  var input_id = $('#input-value-label').text();  
  var value = $('#input-value-form').val();

  updateRunningValue(value)
  processValue(input_id, value)
}






function getUnitClass(s) {
  if (s in input_value_dict) {
    v = input_value_dict[s]
    if (v == EMPTY_VAL) {
      return 'btn-outline-secondary'
    }
    if (v == null) {
      return 'btn-outline-success'
    }
  }
  
  return 'btn-outline-primary'
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
function setupDynamicValue(input_id) {
  // Fetch the options
  options = OPTIONS_DICT[input_id]

  // Fill options
  if (options && options.length > 0) {
    console.log('gotcha')
    fillDynamicOptions(input_id, options)
  }

  $('#value-entry-container').show();
  $('#input-value-label').text(input_id);  
}

// User selects an input type
function handleInputClick(input_id) {
  value = input_value_dict[input_id]
  
  if (value == EMPTY_VAL) {
    // Empty unit
    processValue(input_id, null)
  } else if (value) {
    // Static unit
    updateRunningValue(value)
    processValue(input_id, value)    
  } else {
    // Dynamic unit
    setupDynamicValue(input_id)
  }
}


// Fill the selection grid with valid units
function presentUnits(units) {
  var $selectionGrid = $('#unit-selection-grid');

  // Clear the existing buttons
  $selectionGrid.empty();

  // Store units in a dict for later
  unit_keys = Object.keys(units)
  OPTIONS_DICT = units

  // Iterate through the strings and create buttons
  // Each button needs a further handler
  $.each(unit_keys, function(index, string) {
    var $button = $('<button>').text(string);
    unit_class = getUnitClass(string)
    $button.addClass('btn');
    $button.addClass('btn-sm');
    $button.addClass('unit-button');
    $button.addClass(unit_class);
    $button.click(function() {
      handleInputClick(string);
    });
    $selectionGrid.append($button);
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
  $('#parameter-submission-container').show()
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