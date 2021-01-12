import React, { Component } from 'react'
import axios from 'axios'
import { string, func } from 'prop-types'
import cx from 'classnames'

import styles from './textInput.scss'


class TextInput extends Component {
  state = {
    value: this.props.value,
    focused: false,
  }

  onClick = () => {
    axios.post('http://0.0.0.0:8000/clean/', {
      pub_id: 'ABC123',
      abstract: this.state.value
    })
    .then((response) => {
      console.log(response)
      this.setState({ value: `[${response.data.clean_abstract}]` })
    }, (error) => {
      console.log(error)
    })
  }

  onChange = event => {
    const { target: { value } } = event
    this.setState({ value })
    if (this.props.onChange) this.props.onChange(event)
  }

  render () {
    const { onChange, onClick } = this
    const { label, className, ...props } = this.props
    const { value, focused } = this.state
    return (
      <div
        className={cx(
          styles.container,
          (focused || value.length) && styles.active,
          focused && styles.focused,
        )}
      >
        {label && (
          <label
            htmlFor={id}
            className={styles.label}
          >{label}</label>
        )}
        <input
          {...props}
          className={cx(styles.input, className)}
          onChange={onChange}
          value={value}
        />
        <input
          type="button"
          value="Click to transform the text input"
          onClick={onClick}
        />
      </div>
    )
  }
}

TextInput.propTypes = {
  label: string,
  className: string,
  onChange: func,
  onClick: func,
  value: string,
}

TextInput.defaultProps = {
  label: undefined,
  className: undefined,
  onChange: undefined,
  onClick: undefined,
  value: '',
}

export default TextInput

